#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x3570DA17270ACE24 (sergeh@kernel.org)
#
Name     : shadow
Version  : 4.13
Release  : 68
URL      : https://github.com/shadow-maint/shadow/releases/download/4.13/shadow-4.13.tar.xz
Source0  : https://github.com/shadow-maint/shadow/releases/download/4.13/shadow-4.13.tar.xz
Source1  : https://github.com/shadow-maint/shadow/releases/download/4.13/shadow-4.13.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: shadow-bin = %{version}-%{release}
Requires: shadow-data = %{version}-%{release}
Requires: shadow-lib = %{version}-%{release}
Requires: shadow-license = %{version}-%{release}
Requires: shadow-locales = %{version}-%{release}
Requires: shadow-man = %{version}-%{release}
Requires: Linux-PAM-bin
Requires: Linux-PAM-lib
BuildRequires : Linux-PAM-dev
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : gdb
BuildRequires : libcap-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Make-usermod-read-altfiles.patch
Patch2: 0002-Allow-lower-case-n-for-n-group.patch
Patch3: 0003-stateless-configs.patch
Patch4: 0004-Use-correct-pam.d-path.patch
Patch5: 0005-Enable-stateless-login.patch
Patch6: 0006-Enable-statless-useradd-command.patch
Patch7: 0007-Enable-statless-gpasswd.patch
Patch8: 0008-Enable-stateless-usermod-command.patch
Patch9: 0009-Make-glibc-give-up-memory-we-have-already-released.patch
Patch10: 0010-Add-pam-files.patch
Patch11: 0011-set-umask-to-027.patch
Patch12: 0012-Update-stateless-for-shadow-4.13.patch
Patch13: backport-contral-char-check.patch
Patch14: backport-overhaul-valid-field.patch

%description
# shadow-utils
## Introduction
The shadow-utils package includes the necessary programs for
converting UNIX password files to the shadow password format, plus
programs for managing user and group accounts. The pwconv command
converts passwords to the shadow password format. The pwunconv command
unconverts shadow passwords and generates a passwd file (a standard
UNIX password file). The pwck command checks the integrity of password
and shadow files. The lastlog command prints out the last login times
for all users. The useradd, userdel, and usermod commands are used for
managing user accounts. The groupadd, groupdel, and groupmod commands
are used for managing group accounts.

%package bin
Summary: bin components for the shadow package.
Group: Binaries
Requires: shadow-data = %{version}-%{release}
Requires: shadow-license = %{version}-%{release}

%description bin
bin components for the shadow package.


%package data
Summary: data components for the shadow package.
Group: Data

%description data
data components for the shadow package.


%package dev
Summary: dev components for the shadow package.
Group: Development
Requires: shadow-lib = %{version}-%{release}
Requires: shadow-bin = %{version}-%{release}
Requires: shadow-data = %{version}-%{release}
Provides: shadow-devel = %{version}-%{release}
Requires: shadow = %{version}-%{release}

%description dev
dev components for the shadow package.


%package lib
Summary: lib components for the shadow package.
Group: Libraries
Requires: shadow-data = %{version}-%{release}
Requires: shadow-license = %{version}-%{release}

%description lib
lib components for the shadow package.


%package license
Summary: license components for the shadow package.
Group: Default

%description license
license components for the shadow package.


%package locales
Summary: locales components for the shadow package.
Group: Default

%description locales
locales components for the shadow package.


%package man
Summary: man components for the shadow package.
Group: Default

%description man
man components for the shadow package.


%prep
%setup -q -n shadow-4.13
cd %{_builddir}/shadow-4.13
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
%patch -P 6 -p1
%patch -P 7 -p1
%patch -P 8 -p1
%patch -P 9 -p1
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 13 -p1
%patch -P 14 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1689881325
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%reconfigure --disable-static --with-libpam \
--without-libcrack \
--without-selinux \
--enable-nls \
--disable-rpath \
--with-acl \
--with-attr \
--with-group-name-max-length=32 \
--sysconfdir=%{_sysconfdir}
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1689881325
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/shadow
cp %{_builddir}/shadow-%{version}/COPYING %{buildroot}/usr/share/package-licenses/shadow/3dea080ea3c042311fbee5ac2a597e0453b5b924 || :
%make_install
%find_lang shadow
## Remove excluded files
rm -f %{buildroot}*/usr/bin/login
rm -f %{buildroot}*/usr/bin/su
rm -f %{buildroot}*/etc/login.defs
rm -f %{buildroot}*/etc/pam.d/login
rm -f %{buildroot}*/etc/pam.d/su
rm -f %{buildroot}*/usr/share/pam.d/login
rm -f %{buildroot}*/usr/share/pam.d/su
## install_append content
# Defaults are compiled in
rm -f %{buildroot}%{_sysconfdir}/default/useradd
rm -f %{buildroot}%{_sysconfdir}/login.defs

# instal PAM files
install -d %{buildroot}/usr/share/pam.d/
install -m 0644 pam.d/* %{buildroot}/usr/share/pam.d/

# Handle link properly after rename, otherwise missing files would
# lead rpm failed dependencies.
ln -sf newgrp %{buildroot}/usr/bin/sg

pushd man
DESTDIR=%{buildroot} make install-man
popd
# clean up translated versions of these
find %{buildroot}/usr/share/man/ -type f \( -name su.1 -o -name groups.1 -o -name login.1 \) -exec rm {} \;
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/chage
/usr/bin/chfn
/usr/bin/chgpasswd
/usr/bin/chpasswd
/usr/bin/chsh
/usr/bin/expiry
/usr/bin/faillog
/usr/bin/getsubids
/usr/bin/gpasswd
/usr/bin/groupadd
/usr/bin/groupdel
/usr/bin/groupmems
/usr/bin/groupmod
/usr/bin/groups
/usr/bin/grpck
/usr/bin/grpconv
/usr/bin/grpunconv
/usr/bin/lastlog
/usr/bin/logoutd
/usr/bin/newgidmap
/usr/bin/newgrp
/usr/bin/newuidmap
/usr/bin/newusers
/usr/bin/nologin
/usr/bin/passwd
/usr/bin/pwck
/usr/bin/pwconv
/usr/bin/pwunconv
/usr/bin/sg
/usr/bin/useradd
/usr/bin/userdel
/usr/bin/usermod
/usr/bin/vigr
/usr/bin/vipw

%files data
%defattr(-,root,root,-)
/usr/share/pam.d/chfn
/usr/share/pam.d/chpasswd
/usr/share/pam.d/chsh
/usr/share/pam.d/groupmems
/usr/share/pam.d/newusers
/usr/share/pam.d/passwd

%files dev
%defattr(-,root,root,-)
/usr/include/shadow/subid.h
/usr/lib64/libsubid.so
/usr/share/man/man3/getspnam.3
/usr/share/man/man3/shadow.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsubid.so.4
/usr/lib64/libsubid.so.4.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/shadow/3dea080ea3c042311fbee5ac2a597e0453b5b924

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/chage.1
/usr/share/man/man1/chfn.1
/usr/share/man/man1/chsh.1
/usr/share/man/man1/expiry.1
/usr/share/man/man1/getsubids.1
/usr/share/man/man1/gpasswd.1
/usr/share/man/man1/newgidmap.1
/usr/share/man/man1/newgrp.1
/usr/share/man/man1/newuidmap.1
/usr/share/man/man1/passwd.1
/usr/share/man/man1/sg.1
/usr/share/man/man5/faillog.5
/usr/share/man/man5/gshadow.5
/usr/share/man/man5/login.defs.5
/usr/share/man/man5/passwd.5
/usr/share/man/man5/shadow.5
/usr/share/man/man5/suauth.5
/usr/share/man/man5/subgid.5
/usr/share/man/man5/subuid.5
/usr/share/man/man8/chgpasswd.8
/usr/share/man/man8/chpasswd.8
/usr/share/man/man8/faillog.8
/usr/share/man/man8/groupadd.8
/usr/share/man/man8/groupdel.8
/usr/share/man/man8/groupmems.8
/usr/share/man/man8/groupmod.8
/usr/share/man/man8/grpck.8
/usr/share/man/man8/grpconv.8
/usr/share/man/man8/grpunconv.8
/usr/share/man/man8/lastlog.8
/usr/share/man/man8/logoutd.8
/usr/share/man/man8/newusers.8
/usr/share/man/man8/nologin.8
/usr/share/man/man8/pwck.8
/usr/share/man/man8/pwconv.8
/usr/share/man/man8/pwunconv.8
/usr/share/man/man8/useradd.8
/usr/share/man/man8/userdel.8
/usr/share/man/man8/usermod.8
/usr/share/man/man8/vigr.8
/usr/share/man/man8/vipw.8

%files locales -f shadow.lang
%defattr(-,root,root,-)

