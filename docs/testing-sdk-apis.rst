Testing SDK APIs Locally
========================

This guide shows typed SDK usage for every API group exposed by ``openedx-platform-sdk``.
All examples assume you have a running devstack or Tutor instance and an OAuth2 application
configured as described in the `Testing Locally <../README.md#testing-locally>`_ section of
the README.

.. contents:: APIs covered
   :local:
   :depth: 1

----

Setup
-----

Install the SDK in editable mode and configure credentials:

.. code-block:: python

    from openedx_platform_sdk import OAuth2ClientCredentials

    auth = OAuth2ClientCredentials(
        lms_url="http://local.openedx.io:8000",
        client_id="your-client-id",
        client_secret="your-client-secret",
    )

    STUDIO_URL = "http://studio.local.openedx.io:8001/api/contentstore"

    # All examples below run inside this context manager
    with auth.get_client(studio_url=STUDIO_URL) as client:
        ...

.. note::

   ``studio_url`` **must** include ``/api/contentstore``.
   The SDK appends versioned paths (e.g. ``/v3/home/``) directly to this base.

----

Home v3
-------

Retrieve the Studio home page (studio name, course list, library list):

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_retrieve

    with auth.get_client(studio_url=STUDIO_URL) as client:
        home = v3_home_retrieve.sync(client=client)

        print(home.studio_name)     # e.g. "Your Studio"
        print(home.courses)         # list of course summaries
        print(home.libraries)       # list of library summaries

Retrieve only courses (lighter response):

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_courses_retrieve

    with auth.get_client(studio_url=STUDIO_URL) as client:
        result = v3_home_courses_retrieve.sync(client=client)

        for course in result.courses:
            print(course.course_key, course.display_name)

Retrieve only libraries:

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v3_home_libraries_retrieve

    with auth.get_client(studio_url=STUDIO_URL) as client:
        result = v3_home_libraries_retrieve.sync(client=client)

        for lib in result.libraries:
            print(lib.library_key, lib.display_name)

----

Home v4 (paginated courses)
----------------------------

The v4 endpoint returns a paginated wrapper with ``count``, ``num_pages``, ``current_page``,
``start``, ``next_``, ``previous``, and a ``results`` object that holds the course list:

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v4_home_courses_retrieve

    with auth.get_client(studio_url=STUDIO_URL) as client:
        page = v4_home_courses_retrieve.sync(client=client)

        print(f"Total courses : {page.count}")
        print(f"Total pages   : {page.num_pages}")
        print(f"Current page  : {page.current_page}")

        for course in page.results.courses:
            print(course.course_key, course.display_name)

.. note::

   ``page.results`` is a single ``CourseHomeTabSerializerV2`` object — it is *not* a list.
   Iterate ``page.results.courses`` (a list) to reach individual courses.

----

Course Details v3
-----------------

Retrieve course details
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v3_course_details_retrieve

    COURSE_KEY = "course-v1:org+course+run"

    with auth.get_client(studio_url=STUDIO_URL) as client:
        details = v3_course_details_retrieve.sync(client=client, course_id=COURSE_KEY)

        print(details.course_id)
        print(details.org)
        print(details.self_paced)
        print(details.start_date)
        print(details.end_date)

Update course details (PUT round-trip)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The update endpoint expects a full ``CourseDetails`` object. The simplest pattern is to
retrieve first, mutate what you need, then PUT it back:

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import (
        v3_course_details_retrieve,
        v3_course_details_update,
    )

    COURSE_KEY = "course-v1:org+course+run"

    with auth.get_client(studio_url=STUDIO_URL) as client:
        details = v3_course_details_retrieve.sync(client=client, course_id=COURSE_KEY)

        # Toggle self-paced flag
        details.self_paced = not details.self_paced

        updated = v3_course_details_update.sync(
            client=client,
            course_id=COURSE_KEY,
            body=details,
        )
        print(updated.self_paced)   # reflects the new value

----

Authoring Grading v3
---------------------

The grading PATCH endpoint requires ``grade_cutoffs`` and ``grace_period`` in the request body
even though they are not part of the generated ``PatchedauthoringGradingCourseGradingV0`` schema.
Pass them via ``additional_properties``:

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v3_authoring_grading_partial_update
    from openedx_platform_sdk.models.authoring_grading_graders_v0 import AuthoringGradingGradersV0
    from openedx_platform_sdk.models.patchedauthoring_grading_course_grading_v0 import (
        PatchedauthoringGradingCourseGradingV0,
    )

    COURSE_KEY = "course-v1:org+course+run"

    with auth.get_client(studio_url=STUDIO_URL) as client:
        body = PatchedauthoringGradingCourseGradingV0(
            graders=[
                AuthoringGradingGradersV0(
                    type_="Homework",
                    min_count=1,
                    drop_count=0,
                    weight=100,
                    id=0,
                    short_label="HW",
                )
            ],
            grade_cutoffs={"Pass": 0.5},
            grace_period={"hours": 0, "minutes": 0},
            minimum_grade_credit=0.7,
        )

        result = v3_authoring_grading_partial_update.sync(
            client=client,
            course_key=COURSE_KEY,
            body=body,
        )
        print(result.graders)        # list of grader dicts
        print(result.grade_cutoffs)  # {"Pass": 0.5}

.. note::

   ``grade_cutoffs`` and ``grace_period`` are required by ``CourseGradingModel.update_from_json``
   on the platform — always include them in every PATCH even though the endpoint is partial-update.

----

XBlock v1
----------

Retrieve an XBlock
~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v1_xblock_retrieve

    COURSE_USAGE_KEY = "block-v1:org+course+run+type@course+block@course"

    with auth.get_client(studio_url=STUDIO_URL) as client:
        xblock = v1_xblock_retrieve.sync(
            client=client,
            usage_key_string=COURSE_USAGE_KEY,
        )
        print(xblock.id)            # usage key
        print(xblock.category)      # "course"
        print(xblock.display_name)

Create an XBlock
~~~~~~~~~~~~~~~~

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v1_xblock_create
    from openedx_platform_sdk.models.xblock import Xblock

    COURSE_USAGE_KEY = "block-v1:org+course+run+type@course+block@course"

    with auth.get_client(studio_url=STUDIO_URL) as client:
        body = Xblock(
            parent_locator=COURSE_USAGE_KEY,
            category="chapter",
            display_name="My New Section",
        )
        # Use sync_detailed to inspect the status code
        resp = v1_xblock_create.sync_detailed(client=client, body=body)

        print(resp.status_code.value)   # 200
        locator = resp.parsed.additional_properties.get("locator")
        print(locator)                  # usage key of the new block

Update (partial) an XBlock
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v1_xblock_partial_update
    from openedx_platform_sdk.models.patched_xblock import PatchedXblock

    with auth.get_client(studio_url=STUDIO_URL) as client:
        body = PatchedXblock(display_name="Renamed Section")
        resp = v1_xblock_partial_update.sync_detailed(
            client=client,
            usage_key_string=locator,   # locator from the create step above
            body=body,
        )
        print(resp.status_code.value)   # 200

Delete an XBlock
~~~~~~~~~~~~~~~~

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import v1_xblock_destroy

    with auth.get_client(studio_url=STUDIO_URL) as client:
        resp = v1_xblock_destroy.sync_detailed(
            client=client,
            usage_key_string=locator,
        )
        print(resp.status_code.value)   # 204

Full XBlock lifecycle (create → rename → delete)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    from openedx_platform_sdk.api.openedx_platform_sdk import (
        v1_xblock_create,
        v1_xblock_destroy,
        v1_xblock_partial_update,
    )
    from openedx_platform_sdk.models.patched_xblock import PatchedXblock
    from openedx_platform_sdk.models.xblock import Xblock

    COURSE_USAGE_KEY = "block-v1:org+course+run+type@course+block@course"

    with auth.get_client(studio_url=STUDIO_URL) as client:
        # 1. Create
        resp = v1_xblock_create.sync_detailed(
            client=client,
            body=Xblock(
                parent_locator=COURSE_USAGE_KEY,
                category="chapter",
                display_name="Temp Section",
            ),
        )
        locator = resp.parsed.additional_properties["locator"]

        # 2. Rename
        v1_xblock_partial_update.sync_detailed(
            client=client,
            usage_key_string=locator,
            body=PatchedXblock(display_name="Temp Section (Renamed)"),
        )

        # 3. Delete
        v1_xblock_destroy.sync_detailed(
            client=client,
            usage_key_string=locator,
        )

----

Running the Integration Test Suite
------------------------------------

A ready-made integration test script covering all of the above is located at the repo root:

.. code-block:: bash

    cd /path/to/nightly
    pip install -e openedx-platform-sdk/
    python test_sdk.py

Expected output (all 27 checks green)::

    ─── Home v3 ───
    [PASS] v3_home_retrieve returns a result
    [PASS] v3_home_retrieve has studio_name
    [PASS] v3_home_retrieve has courses list
    [PASS] v3_home_courses_retrieve returns a result
    ...
    Results: 27/27 tests passed
    All tests passed!
