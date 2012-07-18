%{!?python_sitelib: %global python_sitelib %(%{__python} -c "import distutils.sysconfig as d; print d.get_python_lib()")}

%define debug_package %{nil}

Summary: Tools for building Appliances
Name: appliance-tools
Version: 006.1
Release: 4%{?dist}
License: GPLv2
Group: System Environment/Base
URL: http://thincrust.org/
# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  git clone git://git.fedorahosted.org/appliance-tools
#  cd appliance-tools
#  git checkout appliance-tools-006.1
#  make dist
Source0: %{name}-%{version}.tar.bz2
Patch0: 0001-Lets-always-write-out-a-Legacy-grub-config-file-sinc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
Requires: livecd-tools >= 020 curl rsync kpartx
Requires: zlib
Requires: qemu-img
BuildRequires: python
BuildArch: noarch
ExcludeArch: ppc64 s390 s390x


%description
Tools for generating appliance images on Fedora based systems including
derived distributions such as RHEL, CentOS and others.
See http://thincrust.net for more details.

%package minimizer
Summary: Tool to minimize a appliance image
Group: System Environment/Base
BuildArch: noarch

%description minimizer
Tool that helps remove unwanted files from the appliance image.

%prep
%setup -q
%patch0 -p1 

%build
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README COPYING
%doc config/fedora-aos.ks
%{_mandir}/man*/*
%{_bindir}/appliance-creator
%{_bindir}/ec2-converter
%dir %{python_sitelib}/appcreate
%dir %{python_sitelib}/ec2convert
%{python_sitelib}/appcreate/*.py
%{python_sitelib}/appcreate/*.pyo
%{python_sitelib}/appcreate/*.pyc
%{python_sitelib}/ec2convert/*.py
%{python_sitelib}/ec2convert/*.pyo
%{python_sitelib}/ec2convert/*.pyc

%files minimizer
%defattr(-,root,root,-)
%doc COPYING
%{_bindir}/image-minimizer

%changelog
* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Feb 13 2012 Dennis Gilmore <dennis@ausil.us> - 006.1-3
- add patch to always write out a legacy grub config file

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 006.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 11 2011 Marek Goldmann <mgoldman@redhat.com> - 006.1-1
- Upstream release 006.1
- Search for grub files also in ARCH-pc directories

* Fri Nov 11 2011 Marek Goldmann <mgoldman@redhat.com> - 006-1
- Support for GRUB2 rhbz#744390
- Align partitions by default
- Search for grub files also in ARCH-unknown directories
- Allow to build appliances without GRUB installed at all

* Sat Oct 29 2011 Dennis Gilmore <dennis@ausil.us> - 005-1.nogrubhack.2
- update hack to work around no grub being installed so we can compose ec2 images

* Sat Oct 29 2011 Dennis Gilmore <dennis@ausil.us> - 005-1.nogrubhack
- add a hack to work around no grub being installed so we can compose ec2 images

* Mon Apr 04 2011 Alan Pevec <apevec@redhat.com> 005-1
- image-minimizer: support drop-keep-drop
- image-minimizer: add droprpm/keeprpm
- Added sub-package for image minimizer (dhuff)

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 004.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Aug 20 2010 Adam Tkac <atkac redhat com> - 004.5-1
- rebuild to ensure NVR in F14 is bigger than in F13
- merge following changes from F12 branch [David Huff]:
  - Fixed error while installing grub
  - Fixed issue with Fedora 12 using dracut to generate initrd
  - Fixed issue with Fedora 12 parted error

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 004.4-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 004.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

*Mon Jul 07 2009 David Huff <dhuff@redhat.com> -004.4
- added functionality include additional modules in ramdisk 

*Mon Dec 01 2008 David Huff <dhuff@redhat.com> -004.2
- changed form ExclusiveArch to EcludeArch to fix broken deps

*Mon Dec 01 2008 David Huff <dhuff@redhat.com> - 004
- bumped version for rebuild for Python 2.6
- Allow the user to pass in --version and --release command line paramneters (bkearney)
- Patches to integrate ec2 conversion into the adk (bkeareny)
- Allow the appliance-creator to use remote urls with the new image tools (bkearney)

*Fri Nov 14 2008 David Huff <dhuff@redhat.com> - 003.9
- Fixed bug in globbing files under a directory (pmyers)

*Fri Nov 14 2008 David Huff <dhuff@redhat.com> - 003.8
- Fixed bug that causes appliance-creator to stacktrace when -i is omitted (pmyers)

*Wed Nov 12 2008 David Huff <dhuff@redhat.com> - 003.7
- Fixed problem with -i only taking one file, now can include a dir
- Fixed versioning of source file, ie. 003.7

*Mon Nov 10 2008 David Huff <dhuff@redhat.com> - 003-6
- Fixed broken dependencies for specific archs where qemu is not available

*Fri Nov 07 2008 David Huff <dhuff@redhat.com> - 003-5
- Added error for Incomplete partition info (#465988)
- Fixed problem with long move operations (#466278)
- Fixed error converting disk formats (#464798)
- Added support for tar archives (#470292)
- Added md5/sha256 disk signature support (jboggs)
- Modified zip functionality can now do with or with out 64bit ext.
- Added support for including extra file in the package (#470337)
- Added option for -o outdir, no longer uses name
- OutPut is now in a seprate dir under appliance name

*Wed Sep 17 2008 David Huff <dhuff@redhat.com> - 003-4
- Removed all the kickstart files in the config dir to mirror livecd-tools
- Added the image minimization to the refactored code (BKearney)
- multiple interface issue (#460922)
- added --format option to specity disk image format
- added --package option to specify output, currently only .zip supported
- added --vmem and --vcpu options
- Merged ec2-converter code (jboggs)

*Tue Aug 26 2008 David Huff <dhuff@redhat.com> - 003-3
- release 3 fixes minor build errors 

* Wed Jul 09 2008 David Huff <dhuff@redhat.com> - 003-1
- version 003 is build for latest version of livecd-tools with patches

* Wed Jul 09 2008 Alan Pevec <apevec@redhat.com> 002-1
- import imgcreate.fs refactoring and other changes
  to make it work with Fedora-9 livecd-tools-0.17.1 w/o Thincrust patches
- version 002 is for f9 branch to work with stock f9 livecd-tools

* Wed Jun 11 2008 David Huff <dhuff@redhat.com> - 001-3
- fixed dependancys

* Tue Jun 10 2008 David Huff <dhuff@redhat.com> - 001-2
- Undated opt parser
- fixed grub issue
- build aginsted newer livecd-tools for selinux issues

* Wed May 14 2008 David Huff <dhuff@redhat.com> - 001
- Initial build.


