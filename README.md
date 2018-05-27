django-download-vendor-files
============================

Setup
-----

Install using pip:

```bash
pip install django-vendor-files
```

Add `download_vendor_files` to `INSTALLED_APPS` in your Django settings:

```python
INSTALLED_APPS = (
    ...
    'vendor_files',
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
