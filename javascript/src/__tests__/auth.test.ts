import { OAuth2ClientCredentials } from '../auth';

const OPTS = {
  lmsUrl: 'https://lms.example.com/',
  clientId: 'id',
  clientSecret: 'secret',
  studioUrl: 'https://studio.example.com/api/contentstore',
};

function mockTokenResponse(token = 'tok-1', expiresIn = 3600) {
  return {
    ok: true,
    status: 200,
    json: async () => ({ access_token: token, expires_in: expiresIn }),
  } as Response;
}

describe('OAuth2ClientCredentials', () => {
  afterEach(() => {
    jest.restoreAllMocks();
  });

  it('requests a token with the client_credentials grant', async () => {
    const fetchMock = jest.fn().mockResolvedValue(mockTokenResponse());
    global.fetch = fetchMock as unknown as typeof fetch;

    const auth = new OAuth2ClientCredentials(OPTS);
    expect(await auth.getToken()).toBe('tok-1');

    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('https://lms.example.com/oauth2/access_token');
    expect(init.method).toBe('POST');
    const body = init.body.toString();
    expect(body).toContain('grant_type=client_credentials');
    expect(body).toContain('token_type=jwt');
  });

  it('caches the token across calls', async () => {
    const fetchMock = jest.fn().mockResolvedValue(mockTokenResponse());
    global.fetch = fetchMock as unknown as typeof fetch;

    const auth = new OAuth2ClientCredentials(OPTS);
    await auth.getToken();
    await auth.getToken();

    expect(fetchMock).toHaveBeenCalledTimes(1);
  });

  it('refetches once the token is inside the refresh buffer', async () => {
    const fetchMock = jest
      .fn()
      .mockResolvedValueOnce(mockTokenResponse('tok-1', 30))
      .mockResolvedValueOnce(mockTokenResponse('tok-2', 3600));
    global.fetch = fetchMock as unknown as typeof fetch;

    const auth = new OAuth2ClientCredentials({ ...OPTS, refreshBufferSeconds: 60 });
    expect(await auth.getToken()).toBe('tok-1');
    expect(await auth.getToken()).toBe('tok-2');
    expect(fetchMock).toHaveBeenCalledTimes(2);
  });

  it('throws when the token endpoint fails', async () => {
    global.fetch = jest.fn().mockResolvedValue({ ok: false, status: 401 }) as unknown as typeof fetch;

    const auth = new OAuth2ClientCredentials(OPTS);
    await expect(auth.getToken()).rejects.toThrow('HTTP 401');
  });

  it('builds a studio client with the JWT prefix', async () => {
    global.fetch = jest.fn().mockResolvedValue(mockTokenResponse()) as unknown as typeof fetch;

    const auth = new OAuth2ClientCredentials(OPTS);
    const client = await auth.getStudioClient();

    expect(client).toBeDefined();
    expect(client.getConfig().headers).toMatchObject({
      Authorization: 'JWT tok-1',
      Accept: 'application/json',
    });
  });

  it('throws from getStudioClient when studioUrl is missing', async () => {
    global.fetch = jest.fn().mockResolvedValue(mockTokenResponse()) as unknown as typeof fetch;

    const auth = new OAuth2ClientCredentials({ ...OPTS, studioUrl: undefined });
    await expect(auth.getStudioClient()).rejects.toThrow('studioUrl must be set');
  });

  it('points the lms client at the enrollment api', async () => {
    global.fetch = jest.fn().mockResolvedValue(mockTokenResponse()) as unknown as typeof fetch;

    const auth = new OAuth2ClientCredentials(OPTS);
    const client = await auth.getLmsClient();

    expect(client.getConfig().baseURL).toBe('https://lms.example.com/api/enrollment');
  });
});
