# PyPiInfo

##PyPi XML-RPC wrapper class

This is a class of wrappers around PyPi's XML-RPC commands

To get started, all you need to do is instanciate the class

```
ppi = PyPiInfo()
```

After that, the wrappers available are:

**get_package_list(self)**

    Retrieve a list of the package names registered with the package index. Returns a list of name strings.

```
    # =========================================
    # Get list of all packages
    # =========================================
    #  Don't print out package list, it will contain over 90,000
    #  entries - Use it in a GUI treeview or similar to select
    #  other information
    package_list = ppi.get_package_list()
    time.sleep(.2)
```

**get_releases(self, package_name, hidden=False)**

    Retrieve a list of the releases registered for the given package_name. Returns a list with all version strings if ```

```
    # =========================================
    # Get list containing all release versions
    # =========================================
    print('\n=========================================')
    releases = ppi.get_releases(package_name)
    print('releases: {}'.format(releases))
    time.sleep(.2)
```
  hidden is True or only the non-hidden ones otherwise.
    
**get_package_roles(self, package_name)**

    Retrieve a list of users and their attributes roles for a given package_name. Role is either 'Maintainer' or 'Owner'. 

```
    # =========================================
    # list of users and their attributes roles for package
    # =========================================
    print('\n=========================================')
    package_roles = ppi.get_package_roles(package_name)
    print('package roles: {}'.format(package_roles))
    time.sleep(.2)

```

**get_user_packages(self, user)**

    Retrieve a list of [role_name, package_name] for a given username. Role is either 'Maintainer' or 'Owner'. 

```
    # =========================================
    # list of [role_name, package_name] for a given username
    # =========================================
    print('\n=========================================')
    print('user packages: {}'.format(ppi.get_user_packages(package_roles[0][1])))
    time.sleep(.2)
```

**get_release_downloads(self, package_name, version)**

    Retrieve a list of files and download count for a given package and release version. 

```
    # =========================================
    # list of lists: each list contains filename and download count for each file
    # =========================================
    print('\n=========================================')
    print('release downloads: {}'.format(ppi.get_release_downloads(package_name, releases[0])))
    time.sleep(.2)
```

**get_release_urls(self, package_name, version)**

    Retrieve a list of download URLs for the given package release. Returns a list of dicts with the following keys
    
        :honey_pot: url
        :honey_pot: packagetype ('sdist', 'bdist', etc)
        :honey_pot: filename
        :honey_pot: size
        :honey_pot: md5_digest
        :honey_pot: downloads
        :honey_pot: has_sig
        :honey_pot: python_version (required version, or 'source', or 'any')
        :honey_pot: comment_text 

```
    # =========================================
    # list of dicts of download URLs for the given package release
    # =========================================
    print('\n=========================================')
    release_urls = ppi.get_release_urls(package_name, releases[0])
    for n, urldict in enumerate(release_urls):
        print("Package: {} - Version: {} - Release Url's".format(package_name, releases[n]))
        for key, value in urldict.items():
            print('{}: {}'.format(key, value))
        print()
    # print('release urls: {}'.format(release_urls))
    time.sleep(.2)
```

**get_release_data(self, package_name, version)**

    Retrieve metadata describing a specific package release. Returns a dict with keys for
    
    :honey_pot: name
    :honey_pot: version
    :honey_pot: stable_version
    :honey_pot: author
    :honey_pot: author_email
    :honey_pot: maintainer
    :honey_pot: maintainer_email
    :honey_pot: home_page
    :honey_pot: license
    :honey_pot: summary
    :honey_pot: description
    :honey_pot: keywords
    :honey_pot: platform
    :honey_pot: download_url
    :honey_pot: classifiers (list of classifier strings)
    :honey_pot: requires
    :honey_pot: requires_dist
    :honey_pot: provides
    :honey_pot: requires_external
    :honey_pot: requires_python
    :honey_pot: obsoletes
    :honey_pot: obsoletes_dist
    :honey_pot: project_url
    :honey_pot: docs_url (URL of the packages.python.org docs if they've been supplied)

```
    # =========================================
    # a dict of metadata describing a specific package release
    # =========================================
    print('\n=========================================')
    release_data = ppi.get_release_data(package_name, releases[0])
    print("Package: {} - Version: {} - Release Data".format(package_name, releases[n]))
    for key, value in release_data.items():
        print('{}: {}'.format(key, value))
    print()
    time.sleep(.2)
```

**get_search(self, *command)**

    Search the package database using the indicated search spec.
    
    The spec may include any of the keywords described in the above list (except 'stable_version' and 'classifiers'), for example: {'description': 'spam'} will search description fields. Within the spec, a field's value can be a string or a list of strings (the values within the list are combined with an OR), for example: {'name': ['foo', 'bar']}. Valid keys for the spec dict are listed here. Invalid keys are ignored
    
    :honey_pot: name
    :honey_pot: version
    :honey_pot: author
    :honey_pot: author_email
    :honey_pot: maintainer
    :honey_pot: maintainer_email
    :honey_pot: home_page
    :honey_pot: license
    :honey_pot: summary
    :honey_pot: description
    :honey_pot: keywords
    :honey_pot: platform
    :honey_pot: download_url
    
    Arguments for different fields are combined using either "and" (the default) or "or". Example: search({'name': 'foo', 'description': 'bar'}, 'or'). The results are returned as a list of dicts {'name': package name, 'version': package release version, 'summary': package release summary} 

```
    # =========================================
    # Search the package database using the indicated search spec
    # =========================================
    print('\n=========================================')
    search_packages = ppi.get_search({'name': package_name, 'version': releases[0]})
    for n, search_dict in enumerate(search_packages):
        print("Package: {} - Version: {} - Search Results".format(package_name, releases[n]))
        for key, value in search_dict.items():
            print('{}: {}'.format(key, value))
        print()
    time.sleep(.2)
```

**get_browse(self, classifiers)**

    Retrieve a list of (name, version) pairs of all releases classified with all of the given classifiers. 'classifiers' must be a list of Trove classifier strings. 

```
    # =========================================
    # Retrieve a list of (package_name, version) pairs of all releases classified with all of
    # the given classifiers. 'classifiers' must be a list of Trove classifier strings
    # =========================================
    print('\n=========================================')
    browse_packages = ppi.get_browse([
        # "Topic :: Software Development",
        "Topic :: Scientific/Engineering"
    ])
    print('packages from Browse: Topics Scientific/Engineering\n')
    for package in browse_packages:
        print('Package name: {}, Version: {}'.format(package[0], package[1]))
    time.sleep(.2)
```

**get_changelog(self, since, with_ids=False)**

    Retrieve a list of four-tuples (name, version, timestamp, action), or five-tuple including the serial id if ids are requested, since the given timestamp. All timestamps are UTC values. The argument is a UTC integer seconds since the epoch.
    
```
    # =========================================
    # Retrieve a list of four-tuples (name, version, timestamp, action), or five-tuple
    # including the serial id if ids are requested, since the given timestamp. time=UTC
    # =========================================
    print('\n=========================================')
    timestamp = 1480523283
    changes = ppi.get_changelog(timestamp, True)
    for name, version, timestamp, action, serialid in changes:
        print('name: {}, version: {}, timestamp: {}, action: {}, serialid: {}'
                .format(name, version, timestamp, action, serialid))
    time.sleep(.2)
```

**get_changelog_last_serial(self)**

    Retrieve the last event's serial id. 
    
```
    # =========================================
    # Retrieve the last event's serial id.
    # =========================================
    print('\n=========================================')
    serialid = ppi.get_changelog_last_serial()
    print('changelog: serial id: {}'.format(serialid))
    time.sleep(.2)
```

**get_changelog_since_serial(self, since_serial)**

    Retrieve a list of five-tuples (name, version, timestamp, action, serial) since the event identified by the given serial. All timestamps are UTC values. The argument is a UTC integer seconds since the epoch.
    
```
    # =========================================
    # Retrieve a list of five-tuples (name, version, timestamp, action, serial) since
    # the event identified by the given serial. time=UTC
    # =========================================
    print('\n=========================================')
    print('Changelog since serial: {}'.format(serialid - 10))
    changes = ppi.get_changelog_since_serial(serialid - 10)
    for itemname, version, timestamp, action, serial in changes:
        print('itemname: {}, version: {}, timestamp: {}, action: {}, serial: {}'
              .format(itemname, version, timestamp, action, serial))
    time.sleep(.2)
```

*Credits: Original commands and call descriptions come from from PyPi*
