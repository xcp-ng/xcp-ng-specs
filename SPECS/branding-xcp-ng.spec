Name:           branding-xcp-ng
Version:        1.0.1
Release:        1%{?dist}
Summary:        XCP-ng branding
Group:          System/Hypervisor
License:        ISC
URL:            https://github.com/xcp-ng/branding-xcp-ng
Source0:        https://github.com/xcp-ng/branding-xcp-ng/archive/v%{version}/branding-xcp-ng-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
Requires:       python

%description
This package contains branding information for XCP-ng.

%prep
%autosetup -p1

%install
%{__install} -D -m 0644 branding/branding            %{buildroot}%{_usrsrc}/branding/branding
%{__install} -D -m 0755 branding/brand-directory.py  %{buildroot}%{_usrsrc}/branding/brand-directory.py
%{__install} -D -m 0755 branding/branding-compile.py %{buildroot}%{_usrsrc}/branding/branding-compile.py

%files
%{_usrsrc}/branding/branding
%{_usrsrc}/branding/brand-directory.py
%{_usrsrc}/branding/branding-compile.py
%exclude %{_usrsrc}/branding/*.pyc
%exclude %{_usrsrc}/branding/*.pyo

%changelog
* Thu Jun 21 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.1-1
- Update for XCP-ng 7.5.0
* Sun Apr 29 2018 John Else <john.else@gmail.com> - 1.0.0-1
- Initial package
