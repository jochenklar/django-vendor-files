django-download-vendor-files
============================

Setup
-----

Install using pip:

```bash
pip install django-vendor-files
```

Add `vendor_files` to `INSTALLED_APPS` in your Django settings:

```python
INSTALLED_APPS = (
    ...
    'vendor_files',
)
```

Put the `vendor` directory in `STATICFILES_DIRS` in your Django settings:

```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'vendor/'),
    ...
)
```

Add a `VENDOR` setting to your Django settings, and add your vendor files with URL and SNI, e.g.:

```python
VENDOR = {
    'jquery': {
        'url': 'https://code.jquery.com/',
        'js': [
            {
                'path': 'jquery-3.2.1.min.js',
                'sri': 'sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=',
            }
        ]
    },
    'bootstrap': {
        'url': 'https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/',
        'js': [
            {
                'path': 'js/bootstrap.min.js',
                'sri': 'sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa',
            }
        ],
        'css': [
            {
                'path': 'css/bootstrap.min.css',
                'sri': 'sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u',
            }
        ]
    }
}
```

Usage
-----

Put `{% load vendor_tags %}` at the top of your Django template and the vendor tag , e.g.: `{% vendor 'jquery' %}`, somewhere in your HTML:

```html
{% load staticfiles %}
{% load vendor_tags %}

<!DOCTYPE html>
<html>
    <head>
        <title>{{ request.site.name }}</title>
        ...
        {% vendor 'jquery' %}
        {% vendor 'bootstrap' %}
    </head>
```

 Then, you have 2 options:

1) To use a CDN, put `VENDOR_CDN = True` in your Django settings and the vendor tag will be replaced by a `<link>` or `<script>` tag using the URLs in the settings.

2) To use a local copy, put `VENDOR_CDN = False` (or nothing at all) in your Django settings and the vendor tag will be replaced by a `<link>` or `<script>` tag using your `STATIC_PATH`. The files can be downloaded:

    ```
    python ./manage.py download_vendor_files
    ```
