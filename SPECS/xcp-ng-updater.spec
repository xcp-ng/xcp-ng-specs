Summary: XAPI plugin for updating through yum
Name: xcp-ng-updater
Version: 1.0.0
Release: 1
URL: https://github.com/xcp-ng/xcp-ng-updater
Source0: https://github.com/xcp-ng/xcp-ng-updater/archive/v%{version}/%{name}-%{version}.tar.gz
License: AGPLv3

Group: Applications/System
BuildArch: noarch

%description
A XAPI plugin that allows to interact with the underlying package manager.

%prep
%autosetup -p1

%install
install -D SOURCES/etc/xapi.d/plugins/updater.py %{buildroot}/etc/xapi.d/plugins/updater.py

%files
%doc LICENSE README.md test_plugin.sh
/etc/xapi.d/plugins/*

%changelog
* Fri Jun 29 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-1
- Initial package.

