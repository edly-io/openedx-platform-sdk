import { createClient } from '@hey-api/client-axios';

const TOKEN_ENDPOINT = '/oauth2/access_token';

export interface OAuth2Options {
  lmsUrl: string;
  clientId: string;
  clientSecret: string;
  studioUrl?: string;
  refreshBufferSeconds?: number;
}

export type Client = ReturnType<typeof createClient>;

/**
 * Fetches and caches a JWT from the LMS OAuth2 endpoint, refreshing it
 * `refreshBufferSeconds` before expiry. Open edX expects the "JWT" prefix,
 * not "Bearer".
 */
export class OAuth2ClientCredentials {
  private readonly lmsUrl: string;

  private readonly clientId: string;

  private readonly clientSecret: string;

  private readonly studioUrl: string;

  private readonly refreshBufferSeconds: number;

  private token: string | null = null;

  private expiresAt = 0;

  constructor(options: OAuth2Options) {
    this.lmsUrl = options.lmsUrl.replace(/\/+$/, '');
    this.clientId = options.clientId;
    this.clientSecret = options.clientSecret;
    this.studioUrl = options.studioUrl ?? '';
    this.refreshBufferSeconds = options.refreshBufferSeconds ?? 60;
  }

  private async fetchToken(): Promise<void> {
    const body = new URLSearchParams({
      grant_type: 'client_credentials',
      client_id: this.clientId,
      client_secret: this.clientSecret,
      token_type: 'jwt',
    });

    const response = await fetch(`${this.lmsUrl}${TOKEN_ENDPOINT}`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body,
    });

    if (!response.ok) {
      throw new Error(`Failed to obtain access token: HTTP ${response.status}`);
    }

    const data = (await response.json()) as { access_token: string; expires_in?: number };
    this.token = data.access_token;
    this.expiresAt = Date.now() / 1000 + (data.expires_in ?? 3600);
  }

  async getToken(): Promise<string> {
    if (this.token === null || Date.now() / 1000 >= this.expiresAt - this.refreshBufferSeconds) {
      await this.fetchToken();
    }
    return this.token as string;
  }

  async getClient(baseUrl: string, headers: Record<string, string> = {}): Promise<Client> {
    const token = await this.getToken();
    return createClient({
      baseURL: baseUrl.replace(/\/+$/, ''),
      headers: {
        Accept: 'application/json',
        Authorization: `JWT ${token}`,
        ...headers,
      },
    });
  }

  async getStudioClient(headers?: Record<string, string>): Promise<Client> {
    if (!this.studioUrl) {
      throw new Error('studioUrl must be set on OAuth2ClientCredentials to use getStudioClient()');
    }
    return this.getClient(this.studioUrl, headers);
  }

  async getLmsClient(headers?: Record<string, string>): Promise<Client> {
    return this.getClient(`${this.lmsUrl}/api/enrollment`, headers);
  }
}
