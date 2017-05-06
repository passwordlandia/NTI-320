Name:		check_cool_plugin
Version:	1.0
Release:	1%{?dist}
Summary:	cool new nrpe plugin rpm

Group:		nti320-jwade005
License:	GPL
URL:		github.com/jwade005/nti320/rpm
Source0:	check_cool_plugin-1.0.tar.gz

BuildRequires:
Requires:

BuildRoot: %{_tmppath}/%{name}-buildroot

%description
this is a beta rpm build for a nagios nrpe plugin

%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}
install -m 0755 -d $RPM_BUILD_ROOT/usr/lib64/nagios/plugins/
install -m 0755 check_cool_plugin.sh $RPM_BUILD_ROOT/usr/lib64/nagios/plugins/check_cool_plugin

%clean
rm -rf $RPM_BUILD_ROOT

%post
echo . .
echo .cehck_cool_plugin nagios nrpe plugin installed!.

%files
%dir /usr/lib64/nagios/plugins/
/usr/lib64/nagios/plugins/check_cool_plugin.sh


%doc



%changelog


# check_cool_plugin rpm build

# [Jonathan@rpm-b rpmbuild]$ rpmbuild -ba SPECS/check_cool_plugin.spec
# Executing(%prep): /bin/sh -e /var/tmp/rpm-tmp.BoF8o1
# + umask 022
# + cd /home/Jonathan/rpmbuild/BUILD
# + cd /home/Jonathan/rpmbuild/BUILD
# + rm -rf check_cool_plugin-1.0
# + /usr/bin/mkdir -p check_cool_plugin-1.0
# + cd check_cool_plugin-1.0
# + /usr/bin/gzip -dc /home/Jonathan/rpmbuild/SOURCES/check_cool_plugin-1.0.tar.gz
# + /usr/bin/tar -xf -
# + STATUS=0
# + '[' 0 -ne 0 ']'
# + /usr/bin/chmod -Rf a+rX,u+w,g-w,o-w .
# + exit 0
# Executing(%build): /bin/sh -e /var/tmp/rpm-tmp.LU2U3n
# + umask 022
# + cd /home/Jonathan/rpmbuild/BUILD
# + cd check_cool_plugin-1.0
# + exit 0
# Executing(%install): /bin/sh -e /var/tmp/rpm-tmp.iKiFJK
# + umask 022
# + cd /home/Jonathan/rpmbuild/BUILD
# + '[' /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64 '!=' / ']'
# + rm -rf /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64
# ++ dirname /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64
# + mkdir -p /home/Jonathan/rpmbuild/BUILDROOT
# + mkdir /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64
# + cd check_cool_plugin-1.0
# + install -m 0755 -d /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64/usr/lib64/nagios/plugins/
# + install -m 0755 /home/Jonathan/rpmbuild/SOURCES/plugins/check_cool_plugin /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64/usr/lib64/nagios/plugins/check_cool_plugin
# + /usr/lib/rpm/find-debuginfo.sh --strict-build-id -m --run-dwz --dwz-low-mem-die-limit 10000000 --dwz-max-die-limit 110000000 /home/Jonathan/rpmbuild/BUILD/check_cool_plugin-1.0
# /usr/lib/rpm/sepdebugcrcfix: Updated 0 CRC32s, 0 CRC32s did match.
# + /usr/lib/rpm/check-buildroot
# + /usr/lib/rpm/redhat/brp-compress
# + /usr/lib/rpm/redhat/brp-strip-static-archive /usr/bin/strip
# + /usr/lib/rpm/brp-python-bytecompile /usr/bin/python 1
# + /usr/lib/rpm/redhat/brp-python-hardlink
# + /usr/lib/rpm/redhat/brp-java-repack-jars
# Processing files: check_cool_plugin-1.0-1.el7.centos.x86_64
# Provides: check_cool_plugin = 1.0-1.el7.centos check_cool_plugin(x86-64) = 1.0-1.el7.centos
# Requires(interp): /bin/sh
# Requires(rpmlib): rpmlib(CompressedFileNames) <= 3.0.4-1 rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1
# Requires(post): /bin/sh
# Requires: /bin/bash
# Processing files: check_cool_plugin-debuginfo-1.0-1.el7.centos.x86_64
# Provides: check_cool_plugin-debuginfo = 1.0-1.el7.centos check_cool_plugin-debuginfo(x86-64) = 1.0-1.el7.centos
# Requires(rpmlib): rpmlib(FileDigests) <= 4.6.0-1 rpmlib(PayloadFilesHavePrefix) <= 4.0-1 rpmlib(CompressedFileNames) <= 3.0.4-1
# Checking for unpackaged file(s): /usr/lib/rpm/check-files /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64
# Wrote: /home/Jonathan/rpmbuild/SRPMS/check_cool_plugin-1.0-1.el7.centos.src.rpm
# Wrote: /home/Jonathan/rpmbuild/RPMS/x86_64/check_cool_plugin-1.0-1.el7.centos.x86_64.rpm
# Wrote: /home/Jonathan/rpmbuild/RPMS/x86_64/check_cool_plugin-debuginfo-1.0-1.el7.centos.x86_64.rpm
# Executing(%clean): /bin/sh -e /var/tmp/rpm-tmp.l8cZqk
# + umask 022
# + cd /home/Jonathan/rpmbuild/BUILD
# + cd check_cool_plugin-1.0
# + rm -rf /home/Jonathan/rpmbuild/BUILDROOT/check_cool_plugin-1.0-1.el7.centos.x86_64
# + exit 0
# [Jonathan@rpm-b rpmbuild]$ ls
# BUILD  BUILDROOT  RPMS  SOURCES  SPECS  SRPMS
# [Jonathan@rpm-b rpmbuild]$ cd RPMS
# [Jonathan@rpm-b RPMS]$ ls
# x86_64
# [Jonathan@rpm-b RPMS]$ tree
# .
# └── x86_64
#     ├── check_cool_plugin-1.0-1.el7.centos.x86_64.rpm
#     └── check_cool_plugin-debuginfo-1.0-1.el7.centos.x86_64.rpm
#
# 1 directory, 2 files
# [Jonathan@rpm-b RPMS]$
