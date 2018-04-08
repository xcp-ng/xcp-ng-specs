Name:           xcp-featured
Version:        1.0.1
Release:        1%{?dist}
Summary:        XCP-ng feature daemon
Group:          System/Hypervisor
License:        ISC
URL:            https://github.com/xcp-ng/xcp-featured
Source0:        https://github.com/xcp-ng/xcp-featured/archive/v%{version}/xcp-featured-%{version}.tar.gz
Source1:        v6d.service
BuildRoot:      %{_tmppath}/%{name}-%{version}-root
BuildRequires:  systemd
BuildRequires:  xs-opam-repo
BuildRequires:  ocaml-xcp-idl-devel
BuildRequires:  xapi-client-devel

%description
This package contains an RPC serving daemon, which reports the features
available on an xcp-ng host.

%prep
%autosetup -p1

%build
DESTDIR=%{buildroot} %{__make}

%install
DESTDIR=%{buildroot} LIBEXECDIR=%{_libexecdir} %{__make} install
%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/v6d.service

%post
ln -fs %{_libexecdir}/xcp-featured %{_libexecdir}/v6d
%systemd_post v6d.service

%preun
%systemd_preun v6d.service

%postun
%systemd_postun v6d.service
rm -f %{_libexecdir}/v6d

%files
%ghost %{_libexecdir}/v6d
%{_libexecdir}/xcp-featured
%{_unitdir}/v6d.service

%changelog
* Mon Apr 09 2018 John Else <john.else@gmail.com> - 1.0.1-1
- Add additional feature flags

* Sun Mar 25 2018 John Else <john.else@gmail.com> - 1.0.0-1
- Initial package
