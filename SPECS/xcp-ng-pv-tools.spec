%define xs_tools_version 7.29.0
%define xs_tools_release 2

Name: xcp-ng-pv-tools
Version: 7.29.0
Release: 2.2.xcp
Summary: ISO with the Linux PV Tools
License: GPLv2
# Until we're ready to build the tools ourselves, we'll extract the linux tools from XenServer's RPM
Source0: xenserver-pv-tools-%{xs_tools_version}-%{xs_tools_release}.noarch.rpm
Source1: README.txt.patch
BuildArch: noarch
BuildRequires: cpio
BuildRequires: genisoimage
BuildRequires: p7zip-plugins

Provides: xenserver-pv-tools
Obsoletes: xenserver-pv-tools

%define xensource opt/xensource
%define iso_version %{version}-%{release}

%description
ISO with the Linux PV Tools

%prep
%setup -cT

%build
rpm2cpio %{SOURCE0} | cpio -idmv
7z x %{xensource}/packages/iso/guest-tools-*.iso -oiso
chmod u+w iso/ -R
pushd iso
/bin/rm AUTORUN.INF copyright.txt EULA *.exe *.msi
# patch readme
patch -p0 < %{SOURCE1}
popd
# fix exec permissions
pushd iso/Linux
chmod a+x install.sh xe-daemon xe-linux-distribution
popd
genisoimage -joliet -joliet-long -r \
            -A "XCP-ng Tools" \
            -V "XCP-ng Tools" \
            -publisher "XCP-ng community" \
            -o guest-tools.iso \
            iso/

%install
install -D -m644 guest-tools.iso %{buildroot}/%{xensource}/packages/iso/guest-tools-%{iso_version}.iso
install -D -m755 %{xensource}/bin/sr_rescan %{buildroot}/%{xensource}/bin/sr_rescan
install -D -m755 %{xensource}/libexec/unmount_halted_xstools.sh %{buildroot}/%{xensource}/libexec/unmount_halted_xstools.sh

%post
/%{xensource}/libexec/unmount_halted_xstools.sh
/%{xensource}/bin/sr_rescan

%postun
/%{xensource}/bin/sr_rescan

%triggerpostun -- xenserver-pv-tools = 7.0.0.125243c.2061
/%{xensource}/bin/sr_rescan

%clean
rm -rf %{buildroot}

%files
/%{xensource}/packages/iso/
/%{xensource}/bin/
/%{xensource}/libexec/

%changelog
* Fri Aug 03 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.29.0-2.1.xcp
- Update README.txt

* Wed Jun 27 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.29.0-2
- Rename to xp-ng-pv-tools
- Remove proprietary Windows tools

* Tue Apr 17 2018 Ben Chalmers <ben.chalmers@citrix.com> - 7.29.0
- CA-287636: Merge WHQLed Xenbus 8.2.1.124 into product

* Fri Mar 23 2018 Lin Liu<lin.liu@citrix.com - 7.27.0
- CP-27537: SR-IOV feature merge of Windows/Linux guest tools

* Thu Mar 15 2018 Owen Smith <owen.smith@citrix.com - 7.26.0
- CP-25543: Add WHQL XenNet, fixes for CA-279157

* Fri Dec 08 2017 Kun Ma <kun.ma@citrix.com - 7.24.0-1
- CA-275123: Fix PVAddons version

* Wed Sep 20 2017 Ben Chalmers <ben.chalmers@citrix.com - 7.21.0-1
- CP-24583: Synchronise xenserver signed drivers

* Fri Aug 18 2017 Deli Zhang <deli.zhang@citrix.com> - 7.20.0-1
- CP-22495: Add support for NeoKylin Linux Security OS 5.0

* Mon Aug 14 2017 Ben Chalmers <Ben.Chalmers@citrix.com> - v7.19.0-1
- XenVbd 8.2.1.158
- CA-257867: XenVBD Casues VM Hang
- CA-237752: Winodws 7 VM wedged in reboot loop (PdoReset loop)
- XenIface 8.2.1.102
- CA-248924: Excessive logging in windows after resuming from suspend
- XenVif 8.2.1.152
- CA-251602: Xenbus monitor does not seem to be removing reboot key
- Installer 1058
- CA-250167: Fix Interop.*.dll signing

* Thu Jun 08 2017 Wei Xie <wei.xie@citrix.com> - v7.14.0-1
- Update xe-guest-utilities to v7.6.0
- CP-22352: Add support for Yinhe Kylin Linux.
- CP-22351: Add support for Linx.

* Fri Jun 02 2017 Wei Xie <wei.xie@citrix.com> - v7.13.0-1
- Change URLS that contains guest utilities for RedFlag and Turbo Linux.
- CP-22358: Identify Turbo Linux.
- CP-21862: Make guest tools identify RedFlag Linux.
- CA-253166: Do not silently ignore errors in command lists with pipes
- Commit inspur falcon signed tools https://repo.citrite.net:443/xs-local-build/win-installer/Falcon/win-installer-1020/installer-inspur-falcon-signed.tar

* Wed May 17 2017 Kun Ma <kun.ma@citrix.com>
- CA-253658: Use citrix linux-guest-agent for incloudsphere-pv-tools

* Wed Apr 26 2017 Wei Xie <wei.xie@citrix.com>
- CA-250696: Update xe-guest-utilities to make the build number optional.

* Thu Feb 09 2017 Kostas Ladopoulos <konstantinos.ladopoulos@citrix.com>
- Initial packaging for Transformer

* Wed Jun 15 2016 Ben Chalmers <ben.chalmers@citrix.com>
- Scan SRs after uninstalling and installing
- Remove tools iso from halted VMs before changing

* Fri Jun 05 2015 Ross Lagerwall <ross.lagerwall@citrix.com>
- Initial packaging
