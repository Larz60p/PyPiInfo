# PyPi Package Information Wrapper
#
# Wrapper author - Larry McCaig A.K.A. Larz60+ (python-forum.io moderator)
#
import xmlrpc.client as xmlrpclib
import time


class PyPiInfo:
    """
    list_packages()

        Retrieve a list of the package names registered with the package index.
        Returns a list of name strings.

    package_releases(package_name, show_hidden=False)

        Retrieve a list of the releases registered for the given package_name.
         Returns a list with all version strings if show_hidden is True or only
         the non-hidden ones otherwise.

    package_roles(package_name)

        Retrieve a list of users and their attributes roles for a given
         package_name. Role is either 'Maintainer' or 'Owner'.

    user_packages(user)

        Retrieve a list of [role_name, package_name] for a given username.
         Role is either 'Maintainer' or 'Owner'.

    release_downloads(package_name, version)

        Retrieve a list of files and download count for a given package and
         release version.

    release_urls(package_name, version)

        Retrieve a list of download URLs for the given package release. Returns
         a list of dicts with the following keys:

            url
            packagetype ('sdist', 'bdist', etc)
            filename
            size
            md5_digest
            downloads
            has_sig
            python_version (required version, or 'source', or 'any')
            comment_text

    release_data(package_name, version)

        Retrieve metadata describing a specific package release. Returns a dict
         with keys for:

            name
            version
            stable_version
            author
            author_email
            maintainer
            maintainer_email
            home_page
            license
            summary
            description
            keywords
            platform
            download_url
            classifiers (list of classifier strings)
            requires
            requires_dist
            provides
            provides_dist
            requires_external
            requires_python
            obsoletes
            obsoletes_dist
            project_url
            docs_url (URL of the packages.python.org docs if they've been supplied)

        If the release does not exist, an empty dictionary is returned.

    search(spec[, operator])

        Search the package database using the indicated search spec.

        The spec may include any of the keywords described in the above list (except
         'stable_version' and 'classifiers'), for example: {'description': 'spam'}
         will search description fields. Within the spec, a field's value can be a
         string or a list of strings (the values within the list are combined with
         an OR), for example: {'name': ['foo', 'bar']}. Valid keys for the spec dict
         are listed here. Invalid keys are ignored:

            name
            version
            author
            author_email
            maintainer
            maintainer_email
            home_page
            license
            summary
            description
            keywords
            platform
            download_url

        Arguments for different fields are combined using either "and" (the default) or
         "or". Example: search({'name': 'foo', 'description': 'bar'}, 'or'). The results
         are returned as a list of dicts {'name': package name, 'version': package
         release version, 'summary': package release summary}

    browse(classifiers)

        Retrieve a list of (name, version) pairs of all releases classified with all of
         the given classifiers. 'classifiers' must be a list of Trove classifier strings.

    changelog(since, with_ids=False)

        Retrieve a list of four-tuples (name, version, timestamp, action), or five-tuple
         including the serial id if ids are requested, since the given timestamp. All
        timestamps are UTC values. The argument is a UTC integer seconds since the epoch.

    changelog_last_serial()

        Retrieve the last event's serial id.

    changelog_since_serial(since_serial)

        Retrieve a list of five-tuples (name, version, timestamp, action, serial) since
         the event identified by the given serial. All timestamps are UTC values. The
         argument is a UTC integer seconds since the epoch.
    """
    def __init__(self):
        self.client = xmlrpclib.ServerProxy('https://pypi.python.org/pypi')

    def get_package_list(self):
        return self.client.list_packages()

    def get_releases(self, package_name, hidden=False):
        return self.client.package_releases(package_name, hidden)

    def get_package_roles(self, package_name):
        return self.client.package_roles(package_name)

    def get_user_packages(self, user):
        return self.client.user_packages(user)

    def get_release_downloads(self, package_name, version):
        return self.client.release_downloads(package_name, version)

    def get_release_urls(self, package_name, version):
        return self.client.release_urls(package_name, version)

    def get_release_data(self, package_name, version):
        return self.client.release_data(package_name, version)

    def get_search(self, *command):
        return self.client.search(*command)

    def get_browse(self, classifiers):
        return self.client.browse(classifiers)

    def get_changelog(self, since, with_ids=False):
        return self.client.changelog(since, with_ids)

    def get_changelog_last_serial(self):
        return self.client.changelog_last_serial()

    def get_changelog_since_serial(self, since_serial):
        return self.client.changelog_since_serial(since_serial)


if __name__ == '__main__':
    ppi = PyPiInfo()
    # =========================================
    # Example usage
    # =========================================
    #  won't print out package list, it contains over 90,000
    #  entries - Use it in a GUI treeview to select other information
    #  Will use package PyRedstone as default package
    package_list = ppi.get_package_list()
    package_name = 'PyRedstone'
    #
    # =========================================
    # Get list containing all release versions
    print('\n=========================================')
    releases = ppi.get_releases(package_name)
    print('releases: {}'.format(releases))
    time.sleep(.2)

    # =========================================
    # list of users and their attributes roles for package
    print('\n=========================================')
    package_roles = ppi.get_package_roles(package_name)
    print('package roles: {}'.format(package_roles))
    time.sleep(.2)

    # =========================================
    # list of [role_name, package_name] for a given username
    print('\n=========================================')
    print('user packages: {}'.format(ppi.get_user_packages(package_roles[0][1])))
    time.sleep(.2)

    # =========================================
    # list of lists: each list contains filename and download count for each file
    print('\n=========================================')
    print('release downloads: {}'.format(ppi.get_release_downloads(package_name, releases[0])))
    time.sleep(.2)

    # =========================================
    # list of dicts of download URLs for the given package release
    print('\n=========================================')
    release_urls = ppi.get_release_urls(package_name, releases[0])
    for n, urldict in enumerate(release_urls):
        print("Package: {} - Version: {} - Release Url's".format(package_name, releases[n]))
        for key, value in urldict.items():
            print('{}: {}'.format(key, value))
        print()
    # print('release urls: {}'.format(release_urls))
    time.sleep(.2)

    # =========================================
    # a dict of metadata describing a specific package release
    print('\n=========================================')
    release_data = ppi.get_release_data(package_name, releases[0])
    print("Package: {} - Version: {} - Release Data".format(package_name, releases[n]))
    for key, value in release_data.items():
        print('{}: {}'.format(key, value))
    print()
    time.sleep(.2)

    # =========================================
    # Search the package database using the indicated search spec
    print('\n=========================================')
    search_packages = ppi.get_search({'name': package_name, 'version': releases[0]})
    for n, search_dict in enumerate(search_packages):
        print("Package: {} - Version: {} - Search Results".format(package_name, releases[n]))
        for key, value in search_dict.items():
            print('{}: {}'.format(key, value))
        print()
    time.sleep(.2)

    # =========================================
    # Retrieve a list of (package_name, version) pairs of all releases classified with all of
    # the given classifiers. 'classifiers' must be a list of Trove classifier strings
    print('\n=========================================')
    browse_packages = ppi.get_browse([
        # "Topic :: Software Development",
        "Topic :: Scientific/Engineering"
    ])
    print('packages from Browse: Topics Scientific/Engineering\n')
    for package in browse_packages:
        print('Package name: {}, Version: {}'.format(package[0], package[1]))
    time.sleep(.2)

    # =========================================
    # Retrieve a list of four-tuples (name, version, timestamp, action), or five-tuple
    # including the serial id if ids are requested, since the given timestamp. time=UTC
    print('\n=========================================')
    timestamp = 1480523283
    changes = ppi.get_changelog(timestamp, True)
    for name, version, timestamp, action, serialid in changes:
        print('name: {}, version: {}, timestamp: {}, action: {}, serialid: {}'
                .format(name, version, timestamp, action, serialid))
    time.sleep(.2)

    # =========================================
    # Retrieve the last event's serial id.
    print('\n=========================================')
    serialid = ppi.get_changelog_last_serial()
    print('changelog: serial id: {}'.format(serialid))
    time.sleep(.2)

    # =========================================
    # Retrieve a list of five-tuples (name, version, timestamp, action, serial) since
    # the event identified by the given serial. time=UTC
    print('\n=========================================')
    print('Changelog since serial: {}'.format(serialid - 10))
    changes = ppi.get_changelog_since_serial(serialid - 10)
    for itemname, version, timestamp, action, serial in changes:
        print('itemname: {}, version: {}, timestamp: {}, action: {}, serial: {}'
              .format(itemname, version, timestamp, action, serial))
    time.sleep(.2)
