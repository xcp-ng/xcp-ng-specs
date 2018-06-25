# modify the following definitions to match the artifact packaged
# and don't forget to update the changelog at the bottom

%define MAJOR_VERSION  7
%define MINOR_VERSION  5
%define MICRO_VERSION  0
%define BUILD_NUMBER   6297.xcp
%define RELEASE        1
%define PRODUCT        XCP-ng-Center
%define VENDOR_FULL    XCP-ng community

Summary: XCP-ng Center
Name: xencenter
Version: %{MAJOR_VERSION}.%{MINOR_VERSION}.%{MICRO_VERSION}.%{BUILD_NUMBER}
Release: %{RELEASE}
License: BSD 2-Clause
Vendor: %{VENDOR_FULL}
BuildArch: noarch
URL: https://github.com/xcp-ng/xenadmin
Source0: XCP-ng-Center.msi
Source1: XCP-ng-Center.ico
Source2: AUTORUN.INF
BuildRequires: mkisofs

%define iso_dir opt/xensource/packages/iso
%define www_dir opt/xensource/www
%define mnt_dir var/xen/xc-install

%description
Contains the %{PRODUCT} windows installer.

%prep
%setup -cT

%build
cp %{SOURCE0} .
cp %{SOURCE1} .
cp %{SOURCE2} .
mkisofs -J -r -v -publisher "%{VENDOR_FULL}" -p "%{VENDOR_FULL}" -V %{PRODUCT} -o XenCenter.iso .

%install
%{__install} -d %{buildroot}/%{iso_dir}
%{__install} -d %{buildroot}/%{mnt_dir}
%{__install} -d %{buildroot}/%{www_dir}
%{__install} -m 644 XenCenter.iso      %{buildroot}/%{iso_dir}/XenCenter.iso
ln -s /%{iso_dir}/XenCenter.iso        %{buildroot}/%{www_dir}/XenCenter.iso
ln -s /%{mnt_dir}/%{PRODUCT}.msi       %{buildroot}/%{www_dir}/%{PRODUCT}.msi

%pre
if [ $1 -gt 1 ]; then
  # upgrade

  # remove the EXE/msi symlink to prevent XAPI opening it
  rm -f /%{www_dir}/%{PRODUCT}Setup.exe
  rm -f /%{www_dir}/%{PRODUCT}.msi
  # if XAPI already has the EXE/MSI open the unmount will fail, retry a few times
  for i in $(seq 1 10); do
    umount %{mnt_dir} 2>/dev/null && break
    echo "Failed to unmount %{mnt_dir}, retrying..."
    sleep .3
  done
fi

# Use a posttrans script rather than post, old RPMs contained files in %{mnt_dir}
%posttrans
grep -q %{mnt_dir} %{_sysconfdir}/fstab && mount %{mnt_dir}

%files
/%{iso_dir}/XenCenter.iso
%dir /%{mnt_dir}
/%{www_dir}/XenCenter.iso
/%{www_dir}/%{PRODUCT}.msi

%changelog
* Mon Jun 25 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 7.5.0.6297.xcp-1
- Replace XenCenter's installer with that of XCP-ng Center built by the XCP-ng community

* Fri May 11 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.5.0.6297-1
- XenCenter build 6297 on release/kolkata/master: CA-274082, L10N for CP-28097

* Wed May 09 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.5.0.6275-1
- XenCenter build 6275 on release/kolkata/master: SBE build

* Fri Apr 27 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.5.0.6272-1
- XenCenter build 6272 on release/kolkata/master: SBE build

* Fri Apr 27 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.5.0.6268-1
- XenCenter build 6268 on release/kolkata/master: updated product version and the fix for CA-288597

* Wed Apr 25 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6245-1
- XenCenter build 6245 on master: CA-287857

* Mon Apr 23 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6243-1
- XenCenter build 6243 on master: CA-286449, CA-284135, CA-287856, CA-286291, CP-27751

* Tue Apr 17 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6225-1
- XenCenter build 6225 on master: CA-284234, CA-278960, CA-285270; localisation updates (CA-287318, CA-286950, CA-283587, CA-281877), help updates

* Fri Apr 13 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6212-1
- XenCenter build 6212 on master: bugs: CA-287723, CA-287714, CA-287430, CA-287341, CA-287118

* Mon Apr 09 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6202-1
- XenCenter build 6202 on master: bugs and improvements: CP-27568, CA-287498, CA-286574, CA-285215, CA-281881

* Wed Apr 04 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6187-1
- XenCenter build 6187 on master: CP-17099 (SR probe for GFS2) and CA-286582 for REQ-477; bugs and improvements: CA-202377, CA-286293

* Thu Mar 29 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6172-1
- XenCenter build 6172 on master: CA-286458 for REQ-648

* Tue Mar 27 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6165-1
- XenCenter build 6165 on master: CP-26880 for REQ-648; bug fixes for REQ-46 (CA-286137); localisation updates

* Mon Mar 26 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6163-1
- XenCenter build 6163 on master (REQ-46: XenCenter changes for SR-IOV; bugs and improvements: CA-285268, CA-281652)

* Tue Mar 20 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6140-1
- XenCenter build 6140 on master:
- REQ-477: XenCenter changes for GFS2
- improvements for REQ-503: CA-284226, CA-277201, CA-273151
- bugs and improvements: CA-284876, CA-284125, CA-284095, CA-279578, CA-274082, CA-270999


* Thu Mar 01 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.6024-1
- XenCenter build 6024 on master (bug fixes: CA-284234, CA-284233, CA-283697, CA-283613, CA-282014)

* Wed Feb 14 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.4.50.5985-1
- XenCenter build 5985
- Corrections to JsonConverters including CA-283613; added unit tests.
- CA-280329: Fix CrossPoolMigrateDestinationPage with Current Server showing
- CA-281646: Do not download the update again when using an update from disk
- New certificate thumbprints.
- CA-280322: Space requirement calculation error in migration wizard.

* Thu Feb 01 2018 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.4.50.5934-1
- XenCenter build 5934 (JsonRpc backend support) and spec file corrections.

* Mon Jan 22 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.5913-1
- XenCenter build 5913 on master (bug fixes)

* Mon Jan 15 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.5888-1
- XenCenter build 5888 on master (Added Jura XenAPI version, bug fixes)

* Tue Jan 09 2018 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.5872-1
- XenCenter build 5872 on master (licensing changes REQ-637, bug fixes)

* Tue Dec 12 2017 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.4.50.5842-1
- XenCenter build 5842 on master.

* Thu Dec 7 2017 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.4.50.5838-1
- XenCenter build 5838 on master (CA-275576).

* Thu Dec 7 2017 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.4.50.5800-2
- Spec file corrections.

* Thu Nov 30 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.4.50.5800-1
- XenCenter build 5800 on master (product and API version increment, bug fixes)

* Tue Nov 21 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5773-1
- XenCenter build 5773 on master (bug fixes)

* Wed Nov 15 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5757-1
- XenCenter build 5757 on master (bug fixes, localization fixes, updated help)

* Thu Nov 02 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5724-1
- XenCenter build 5724 on master (bug fixes, localization fixes, updated help)

* Wed Oct 25 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5706-1
- XenCenter build 5706 on master (REQ-158, bug fixes, localization fixes)

* Mon Oct 16 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5635-1
- XenCenter build 5635 on master (bug fixes)

* Thu Oct 12 2017 Gabor-Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5629-1
- XenCenter build 5629 on master (REQ-528, bug fixes)

* Thu Oct 05 2017 Gabor-Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5593-1
- XenCenter build 5593 on master (REQ-67, bug fixes)

* Fri Sep 29 2017 Gabor-Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5571-1
- XenCenter build 5571 on master (REQ-411, bug fixes)

* Tue Sep 19 2017 Gabor-Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5526-1
- XenCenter build 5526 on master (REQ-534, REQ-230)

* Mon Sep 11 2017 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5496-1
- XenCenter build 5496 on master (bug fixes)

* Thu Aug 10 2017 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5411-1
- XenCenter build 5411 on master (bug fixes, CAR-473 XC Telemetry)

* Thu Jul 27 2017 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5388-1
- XenCenter build 5388 on master (bug fixes, pool join rules)

* Thu Jul 20 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5355-1
- XenCenter build 5355 on master (bug fixes)

* Tue Jul 11 2017 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.2.50.5311-1
- XenCenter build 5311 on master (switch to the msi installer)

* Wed Jul 05 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5279-1
- XenCenter build 5279 on master (bug fixes + simplified folder structure in the XC build output)

* Tue Jun 27 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5249-1
- XenCenter build 5249 on master (bug fixes)

* Tue Jun 20 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5229-1
- XenCenter build 5229 on master (bug fixes)

* Thu Jun 15 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5194-1
- XenCenter build 5194 on master (Integration of REQ-378 (Support Chinese Language E-mail Performance Alerts) + bug fixes)

* Thu Jun 08 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5183-1
- XenCenter build 5183 on master (Integration of REQ-445 and REQ-446 (Rocky and YinheKylin Linux guest) + CP-21130 (Support for qemu-upstream VNC) + bug fixes)

* Fri Jun 02 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5158-1
- XenCenter build 5158 on master (Integration of REQ-398 and REQ-440: Asianux Linux and Turbo Linux guest templates)

* Thu Jun 01 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5145-1
- XenCenter build 5145 on master (Tagged VLAN integration + bug fixes)

* Mon May 22 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5076-1
- XenCenter build 5076 on master (bug fixes)

* Mon May 15 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.50.5037-1
- XenCenter build 5037 on master (Product version updated to 7.2.50 + bug fixes)

* Fri May 5 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.0.5022-1
- XenCenter build 5022 (Localized help files)

* Thu May 4 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.2.0.4975-1
- XenCenter build 4975 (Product version bumped to 7.2.0)

* Fri Apr 28 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.90.4962-1
- XenCenter build 4962 (Product version bumped to 7.1.90)

* Wed Apr 26 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4954-1
- XenCenter build 4954 (Bug fixes + SBE build)

* Mon Apr 24 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4932-1
- XenCenter build 4932 (Bug fixes)

* Thu Apr 13 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4899-1
- XenCenter build 4899 (Bug fixes)

* Mon Apr 10 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4892-1
- XenCenter build 4892 (Bug fixes)

* Thu Apr 6 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4879-1
- XenCenter build 4879 (Bug fixes + API version increase for Falcon)

* Wed Mar 29 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4856-1
- XenCenter build 4856 (Bug fixes)

* Thu Mar 23 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4836-1
- XenCenter build 4836 (Bug fixes)

* Thu Mar 9 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4792-1
- XenCenter build 4792 (Bug fixes + XenCenter signed with the new certificates)

* Tue Feb 28 2017 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4752-1
- XenCenter build 4752 (Integration of REQ-223: Add Ability to Authenticate to Proxy Server to XenCenter)

* Wed Feb 15 2017 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.1.50.4708-1
- XenCenter build 4708

* Tue Jan 10 2017 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.1.50.4522-1
- XenCenter build 4522

* Wed Dec 21 2016 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.1.50.4472-1
- XenCenter build 4472

* Tue Dec 13 2016 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.1.50.4461-1
- XenCenter build 4461

* Mon Dec 5 2016 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.1.50.4435-1
- XenCenter build 4390

* Mon Nov 28 2016 Mihaela Stoica <mihaela.stoica@citrix.com> - 7.1.50.4390-1
- XenCenter build 4390

* Thu Nov 24 2016 Gabor Apati-Nagy <gabor.apati-nagy@citrix.com> - 7.1.50.4377-1
- XenCenter build 4377

* Thu Nov 24 2016 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.1.50.4359-2
- Bumped XenCenter release number

* Mon Nov 21 2016 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.0.93.4334-2
- Added URL to the spec file

* Tue Nov 15 2016 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.0.93.4334-1
- New release of XenCenter installer

* Thu Nov 3 2016 Konstantina Chremmou <konstantina.chremmou@citrix.com> - 7.0.92.4295-1
- Initial repack of the XenCenter installer
