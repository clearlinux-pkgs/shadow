#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xE9FEEA06A85E3F9D (serge.hallyn@ubuntu.com)
#
Name     : shadow
Version  : 4.6
Release  : 60
URL      : https://github.com/shadow-maint/shadow/releases/download/4.6/shadow-4.6.tar.xz
Source0  : https://github.com/shadow-maint/shadow/releases/download/4.6/shadow-4.6.tar.xz
Source1 : https://github.com/shadow-maint/shadow/releases/download/4.6/shadow-4.6.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 BSD-3-Clause
Requires: shadow-bin = %{version}-%{release}
Requires: shadow-data = %{version}-%{release}
Requires: shadow-license = %{version}-%{release}
Requires: shadow-locales = %{version}-%{release}
Requires: shadow-man = %{version}-%{release}
Requires: Linux-PAM-bin
Requires: Linux-PAM-lib
BuildRequires : Linux-PAM-dev
BuildRequires : acl-dev
BuildRequires : attr-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : gdb
BuildRequires : gettext-bin
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
BuildRequires : util-linux
Patch1: 0001-Make-usermod-read-altfiles.patch
Patch2: 0002-Allow-lower-case-n-for-no-group.patch
Patch3: 0003-shadow-stateless-config.patch
Patch4: 0004-Use-correct-pam.d-path.patch
Patch5: 0005-Enable-stateless-login.patch
Patch6: 0006-Enable-statless-useradd-command.patch
Patch7: 0007-Enable-statless-gpasswd.patch
Patch8: 0008-Enable-stateless-usermod-command.patch
Patch9: 0009-Stateless-files-might-not-exist-in-etc.patch
Patch10: 0010-Make-glibc-give-up-memory-we-have-already-released.patch
Patch11: 0011-Allow-.-inside-usernames-also-allow-uppercase-letter.patch
Patch12: 0012-add-pam-files.patch
Patch13: 0013-set-umask-to-027.patch

%description
Shadow SITES
============
Homepage
http://pkg-shadow.alioth.debian.org/
FTP site
ftp://pkg-shadow.alioth.debian.org/pub/pkg-shadow

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
Requires: shadow-bin = %{version}-%{release}
Requires: shadow-data = %{version}-%{release}
Provides: shadow-devel = %{version}-%{release}
Requires: shadow = %{version}-%{release}

%description dev
dev components for the shadow package.


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
%setup -q -n shadow-4.6
cd %{_builddir}/shadow-4.6
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572545294
export GCC_IGNORE_WERROR=1
export CFLAGS="-O2 -g -Wp,-D_FORTIFY_SOURCE=2 -fexceptions -fstack-protector --param=ssp-buffer-size=32 -Wformat -Wformat-security -Wno-error -Wl,-z,max-page-size=0x1000 -march=westmere -mtune=haswell"
export CXXFLAGS=$CFLAGS
unset LDFLAGS
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 -fstack-protector-strong -mzero-caller-saved-regs=used "
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
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1572545294
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/shadow
cp %{_builddir}/shadow-4.6/COPYING %{buildroot}/usr/share/package-licenses/shadow/b51e7b0e6ab991ba3a9b74fbcc50f7096836f1cb
%make_install
%find_lang shadow
## Remove excluded files
rm -f %{buildroot}/usr/bin/login
rm -f %{buildroot}/usr/bin/su
rm -f %{buildroot}/etc/login.defs
rm -f %{buildroot}/etc/pam.d/login
rm -f %{buildroot}/etc/pam.d/su
rm -f %{buildroot}/usr/share/pam.d/login
rm -f %{buildroot}/usr/share/pam.d/su
## install_append content
rm -f %{buildroot}%{_sysconfdir}/default/useradd
rm -f %{buildroot}%{_sysconfdir}/login.defs
install -d %{buildroot}/usr/share/pam.d/
install -m 0644 pam.d/* %{buildroot}/usr/share/pam.d/
ln -sf newgrp %{buildroot}/usr/bin/sg
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
/usr/share/pam.d/chage
/usr/share/pam.d/chfn
/usr/share/pam.d/chgpasswd
/usr/share/pam.d/chpasswd
/usr/share/pam.d/chsh
/usr/share/pam.d/groupadd
/usr/share/pam.d/groupdel
/usr/share/pam.d/groupmems
/usr/share/pam.d/groupmod
/usr/share/pam.d/newusers
/usr/share/pam.d/passwd
/usr/share/pam.d/useradd
/usr/share/pam.d/userdel
/usr/share/pam.d/usermod

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/getspnam.3
/usr/share/man/man3/shadow.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/shadow/b51e7b0e6ab991ba3a9b74fbcc50f7096836f1cb

%files man
%defattr(0644,root,root,0755)
/usr/share/man/cs/man1/expiry.1
/usr/share/man/cs/man1/gpasswd.1
/usr/share/man/cs/man5/faillog.5
/usr/share/man/cs/man5/gshadow.5
/usr/share/man/cs/man5/passwd.5
/usr/share/man/cs/man5/shadow.5
/usr/share/man/cs/man8/faillog.8
/usr/share/man/cs/man8/groupadd.8
/usr/share/man/cs/man8/groupdel.8
/usr/share/man/cs/man8/groupmod.8
/usr/share/man/cs/man8/grpck.8
/usr/share/man/cs/man8/lastlog.8
/usr/share/man/cs/man8/nologin.8
/usr/share/man/cs/man8/vipw.8
/usr/share/man/da/man1/chfn.1
/usr/share/man/da/man1/newgrp.1
/usr/share/man/da/man1/sg.1
/usr/share/man/da/man5/gshadow.5
/usr/share/man/da/man8/groupdel.8
/usr/share/man/da/man8/logoutd.8
/usr/share/man/da/man8/nologin.8
/usr/share/man/da/man8/vigr.8
/usr/share/man/da/man8/vipw.8
/usr/share/man/de/man1/chage.1
/usr/share/man/de/man1/chfn.1
/usr/share/man/de/man1/chsh.1
/usr/share/man/de/man1/expiry.1
/usr/share/man/de/man1/gpasswd.1
/usr/share/man/de/man1/newgrp.1
/usr/share/man/de/man1/passwd.1
/usr/share/man/de/man1/sg.1
/usr/share/man/de/man3/getspnam.3
/usr/share/man/de/man3/shadow.3
/usr/share/man/de/man5/faillog.5
/usr/share/man/de/man5/gshadow.5
/usr/share/man/de/man5/login.defs.5
/usr/share/man/de/man5/passwd.5
/usr/share/man/de/man5/shadow.5
/usr/share/man/de/man5/suauth.5
/usr/share/man/de/man8/chgpasswd.8
/usr/share/man/de/man8/chpasswd.8
/usr/share/man/de/man8/faillog.8
/usr/share/man/de/man8/groupadd.8
/usr/share/man/de/man8/groupdel.8
/usr/share/man/de/man8/groupmems.8
/usr/share/man/de/man8/groupmod.8
/usr/share/man/de/man8/grpck.8
/usr/share/man/de/man8/grpconv.8
/usr/share/man/de/man8/grpunconv.8
/usr/share/man/de/man8/lastlog.8
/usr/share/man/de/man8/logoutd.8
/usr/share/man/de/man8/newusers.8
/usr/share/man/de/man8/nologin.8
/usr/share/man/de/man8/pwck.8
/usr/share/man/de/man8/pwconv.8
/usr/share/man/de/man8/pwunconv.8
/usr/share/man/de/man8/useradd.8
/usr/share/man/de/man8/userdel.8
/usr/share/man/de/man8/usermod.8
/usr/share/man/de/man8/vigr.8
/usr/share/man/de/man8/vipw.8
/usr/share/man/fi/man1/chfn.1
/usr/share/man/fi/man1/chsh.1
/usr/share/man/fr/man1/chage.1
/usr/share/man/fr/man1/chfn.1
/usr/share/man/fr/man1/chsh.1
/usr/share/man/fr/man1/expiry.1
/usr/share/man/fr/man1/gpasswd.1
/usr/share/man/fr/man1/newgidmap.1
/usr/share/man/fr/man1/newgrp.1
/usr/share/man/fr/man1/newuidmap.1
/usr/share/man/fr/man1/passwd.1
/usr/share/man/fr/man1/sg.1
/usr/share/man/fr/man3/getspnam.3
/usr/share/man/fr/man3/shadow.3
/usr/share/man/fr/man5/faillog.5
/usr/share/man/fr/man5/gshadow.5
/usr/share/man/fr/man5/login.defs.5
/usr/share/man/fr/man5/passwd.5
/usr/share/man/fr/man5/shadow.5
/usr/share/man/fr/man5/suauth.5
/usr/share/man/fr/man5/subgid.5
/usr/share/man/fr/man5/subuid.5
/usr/share/man/fr/man8/chgpasswd.8
/usr/share/man/fr/man8/chpasswd.8
/usr/share/man/fr/man8/faillog.8
/usr/share/man/fr/man8/groupadd.8
/usr/share/man/fr/man8/groupdel.8
/usr/share/man/fr/man8/groupmems.8
/usr/share/man/fr/man8/groupmod.8
/usr/share/man/fr/man8/grpck.8
/usr/share/man/fr/man8/grpconv.8
/usr/share/man/fr/man8/grpunconv.8
/usr/share/man/fr/man8/lastlog.8
/usr/share/man/fr/man8/logoutd.8
/usr/share/man/fr/man8/newusers.8
/usr/share/man/fr/man8/nologin.8
/usr/share/man/fr/man8/pwck.8
/usr/share/man/fr/man8/pwconv.8
/usr/share/man/fr/man8/pwunconv.8
/usr/share/man/fr/man8/useradd.8
/usr/share/man/fr/man8/userdel.8
/usr/share/man/fr/man8/usermod.8
/usr/share/man/fr/man8/vigr.8
/usr/share/man/fr/man8/vipw.8
/usr/share/man/hu/man1/chsh.1
/usr/share/man/hu/man1/gpasswd.1
/usr/share/man/hu/man1/newgrp.1
/usr/share/man/hu/man1/passwd.1
/usr/share/man/hu/man1/sg.1
/usr/share/man/hu/man5/passwd.5
/usr/share/man/hu/man8/lastlog.8
/usr/share/man/id/man1/chsh.1
/usr/share/man/id/man8/useradd.8
/usr/share/man/it/man1/chage.1
/usr/share/man/it/man1/chfn.1
/usr/share/man/it/man1/chsh.1
/usr/share/man/it/man1/expiry.1
/usr/share/man/it/man1/gpasswd.1
/usr/share/man/it/man1/newgrp.1
/usr/share/man/it/man1/passwd.1
/usr/share/man/it/man1/sg.1
/usr/share/man/it/man3/getspnam.3
/usr/share/man/it/man3/shadow.3
/usr/share/man/it/man5/faillog.5
/usr/share/man/it/man5/gshadow.5
/usr/share/man/it/man5/login.defs.5
/usr/share/man/it/man5/passwd.5
/usr/share/man/it/man5/shadow.5
/usr/share/man/it/man5/suauth.5
/usr/share/man/it/man8/chgpasswd.8
/usr/share/man/it/man8/chpasswd.8
/usr/share/man/it/man8/faillog.8
/usr/share/man/it/man8/groupadd.8
/usr/share/man/it/man8/groupdel.8
/usr/share/man/it/man8/groupmems.8
/usr/share/man/it/man8/groupmod.8
/usr/share/man/it/man8/grpck.8
/usr/share/man/it/man8/grpconv.8
/usr/share/man/it/man8/grpunconv.8
/usr/share/man/it/man8/lastlog.8
/usr/share/man/it/man8/logoutd.8
/usr/share/man/it/man8/newusers.8
/usr/share/man/it/man8/nologin.8
/usr/share/man/it/man8/pwck.8
/usr/share/man/it/man8/pwconv.8
/usr/share/man/it/man8/pwunconv.8
/usr/share/man/it/man8/useradd.8
/usr/share/man/it/man8/userdel.8
/usr/share/man/it/man8/usermod.8
/usr/share/man/it/man8/vigr.8
/usr/share/man/it/man8/vipw.8
/usr/share/man/ja/man1/chage.1
/usr/share/man/ja/man1/chfn.1
/usr/share/man/ja/man1/chsh.1
/usr/share/man/ja/man1/expiry.1
/usr/share/man/ja/man1/gpasswd.1
/usr/share/man/ja/man1/newgrp.1
/usr/share/man/ja/man1/passwd.1
/usr/share/man/ja/man1/sg.1
/usr/share/man/ja/man5/faillog.5
/usr/share/man/ja/man5/login.defs.5
/usr/share/man/ja/man5/passwd.5
/usr/share/man/ja/man5/shadow.5
/usr/share/man/ja/man5/suauth.5
/usr/share/man/ja/man8/chpasswd.8
/usr/share/man/ja/man8/faillog.8
/usr/share/man/ja/man8/groupadd.8
/usr/share/man/ja/man8/groupdel.8
/usr/share/man/ja/man8/groupmod.8
/usr/share/man/ja/man8/grpck.8
/usr/share/man/ja/man8/grpconv.8
/usr/share/man/ja/man8/grpunconv.8
/usr/share/man/ja/man8/lastlog.8
/usr/share/man/ja/man8/logoutd.8
/usr/share/man/ja/man8/newusers.8
/usr/share/man/ja/man8/pwck.8
/usr/share/man/ja/man8/pwconv.8
/usr/share/man/ja/man8/pwunconv.8
/usr/share/man/ja/man8/useradd.8
/usr/share/man/ja/man8/userdel.8
/usr/share/man/ja/man8/usermod.8
/usr/share/man/ja/man8/vigr.8
/usr/share/man/ja/man8/vipw.8
/usr/share/man/ko/man1/chfn.1
/usr/share/man/ko/man1/chsh.1
/usr/share/man/ko/man5/passwd.5
/usr/share/man/ko/man8/vigr.8
/usr/share/man/ko/man8/vipw.8
/usr/share/man/man1/chage.1
/usr/share/man/man1/chfn.1
/usr/share/man/man1/chsh.1
/usr/share/man/man1/expiry.1
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
/usr/share/man/pl/man1/chage.1
/usr/share/man/pl/man1/chsh.1
/usr/share/man/pl/man1/expiry.1
/usr/share/man/pl/man1/newgrp.1
/usr/share/man/pl/man1/sg.1
/usr/share/man/pl/man3/getspnam.3
/usr/share/man/pl/man3/shadow.3
/usr/share/man/pl/man5/faillog.5
/usr/share/man/pl/man8/faillog.8
/usr/share/man/pl/man8/groupadd.8
/usr/share/man/pl/man8/groupdel.8
/usr/share/man/pl/man8/groupmems.8
/usr/share/man/pl/man8/groupmod.8
/usr/share/man/pl/man8/grpck.8
/usr/share/man/pl/man8/lastlog.8
/usr/share/man/pl/man8/logoutd.8
/usr/share/man/pl/man8/userdel.8
/usr/share/man/pl/man8/usermod.8
/usr/share/man/pl/man8/vigr.8
/usr/share/man/pl/man8/vipw.8
/usr/share/man/pt_BR/man1/gpasswd.1
/usr/share/man/pt_BR/man5/passwd.5
/usr/share/man/pt_BR/man5/shadow.5
/usr/share/man/pt_BR/man8/groupadd.8
/usr/share/man/pt_BR/man8/groupdel.8
/usr/share/man/pt_BR/man8/groupmod.8
/usr/share/man/ru/man1/chage.1
/usr/share/man/ru/man1/chfn.1
/usr/share/man/ru/man1/chsh.1
/usr/share/man/ru/man1/expiry.1
/usr/share/man/ru/man1/gpasswd.1
/usr/share/man/ru/man1/newgrp.1
/usr/share/man/ru/man1/passwd.1
/usr/share/man/ru/man1/sg.1
/usr/share/man/ru/man3/getspnam.3
/usr/share/man/ru/man3/shadow.3
/usr/share/man/ru/man5/faillog.5
/usr/share/man/ru/man5/gshadow.5
/usr/share/man/ru/man5/login.defs.5
/usr/share/man/ru/man5/passwd.5
/usr/share/man/ru/man5/shadow.5
/usr/share/man/ru/man5/suauth.5
/usr/share/man/ru/man8/chgpasswd.8
/usr/share/man/ru/man8/chpasswd.8
/usr/share/man/ru/man8/faillog.8
/usr/share/man/ru/man8/groupadd.8
/usr/share/man/ru/man8/groupdel.8
/usr/share/man/ru/man8/groupmems.8
/usr/share/man/ru/man8/groupmod.8
/usr/share/man/ru/man8/grpck.8
/usr/share/man/ru/man8/grpconv.8
/usr/share/man/ru/man8/grpunconv.8
/usr/share/man/ru/man8/lastlog.8
/usr/share/man/ru/man8/logoutd.8
/usr/share/man/ru/man8/newusers.8
/usr/share/man/ru/man8/nologin.8
/usr/share/man/ru/man8/pwck.8
/usr/share/man/ru/man8/pwconv.8
/usr/share/man/ru/man8/pwunconv.8
/usr/share/man/ru/man8/useradd.8
/usr/share/man/ru/man8/userdel.8
/usr/share/man/ru/man8/usermod.8
/usr/share/man/ru/man8/vigr.8
/usr/share/man/ru/man8/vipw.8
/usr/share/man/sv/man1/chage.1
/usr/share/man/sv/man1/chsh.1
/usr/share/man/sv/man1/expiry.1
/usr/share/man/sv/man1/newgrp.1
/usr/share/man/sv/man1/passwd.1
/usr/share/man/sv/man1/sg.1
/usr/share/man/sv/man3/getspnam.3
/usr/share/man/sv/man3/shadow.3
/usr/share/man/sv/man5/faillog.5
/usr/share/man/sv/man5/gshadow.5
/usr/share/man/sv/man5/passwd.5
/usr/share/man/sv/man5/suauth.5
/usr/share/man/sv/man8/faillog.8
/usr/share/man/sv/man8/groupadd.8
/usr/share/man/sv/man8/groupdel.8
/usr/share/man/sv/man8/groupmems.8
/usr/share/man/sv/man8/groupmod.8
/usr/share/man/sv/man8/grpck.8
/usr/share/man/sv/man8/lastlog.8
/usr/share/man/sv/man8/logoutd.8
/usr/share/man/sv/man8/nologin.8
/usr/share/man/sv/man8/pwck.8
/usr/share/man/sv/man8/userdel.8
/usr/share/man/sv/man8/vigr.8
/usr/share/man/sv/man8/vipw.8
/usr/share/man/tr/man1/chage.1
/usr/share/man/tr/man1/chfn.1
/usr/share/man/tr/man1/passwd.1
/usr/share/man/tr/man5/passwd.5
/usr/share/man/tr/man5/shadow.5
/usr/share/man/tr/man8/groupadd.8
/usr/share/man/tr/man8/groupdel.8
/usr/share/man/tr/man8/groupmod.8
/usr/share/man/tr/man8/useradd.8
/usr/share/man/tr/man8/userdel.8
/usr/share/man/tr/man8/usermod.8
/usr/share/man/zh_CN/man1/chage.1
/usr/share/man/zh_CN/man1/chfn.1
/usr/share/man/zh_CN/man1/chsh.1
/usr/share/man/zh_CN/man1/expiry.1
/usr/share/man/zh_CN/man1/gpasswd.1
/usr/share/man/zh_CN/man1/newgrp.1
/usr/share/man/zh_CN/man1/passwd.1
/usr/share/man/zh_CN/man1/sg.1
/usr/share/man/zh_CN/man3/getspnam.3
/usr/share/man/zh_CN/man3/shadow.3
/usr/share/man/zh_CN/man5/faillog.5
/usr/share/man/zh_CN/man5/gshadow.5
/usr/share/man/zh_CN/man5/login.defs.5
/usr/share/man/zh_CN/man5/passwd.5
/usr/share/man/zh_CN/man5/shadow.5
/usr/share/man/zh_CN/man5/suauth.5
/usr/share/man/zh_CN/man8/chgpasswd.8
/usr/share/man/zh_CN/man8/chpasswd.8
/usr/share/man/zh_CN/man8/faillog.8
/usr/share/man/zh_CN/man8/groupadd.8
/usr/share/man/zh_CN/man8/groupdel.8
/usr/share/man/zh_CN/man8/groupmems.8
/usr/share/man/zh_CN/man8/groupmod.8
/usr/share/man/zh_CN/man8/grpck.8
/usr/share/man/zh_CN/man8/grpconv.8
/usr/share/man/zh_CN/man8/grpunconv.8
/usr/share/man/zh_CN/man8/lastlog.8
/usr/share/man/zh_CN/man8/logoutd.8
/usr/share/man/zh_CN/man8/newusers.8
/usr/share/man/zh_CN/man8/nologin.8
/usr/share/man/zh_CN/man8/pwck.8
/usr/share/man/zh_CN/man8/pwconv.8
/usr/share/man/zh_CN/man8/pwunconv.8
/usr/share/man/zh_CN/man8/useradd.8
/usr/share/man/zh_CN/man8/userdel.8
/usr/share/man/zh_CN/man8/usermod.8
/usr/share/man/zh_CN/man8/vigr.8
/usr/share/man/zh_CN/man8/vipw.8
/usr/share/man/zh_TW/man1/chfn.1
/usr/share/man/zh_TW/man1/chsh.1
/usr/share/man/zh_TW/man1/newgrp.1
/usr/share/man/zh_TW/man5/passwd.5
/usr/share/man/zh_TW/man8/chpasswd.8
/usr/share/man/zh_TW/man8/groupadd.8
/usr/share/man/zh_TW/man8/groupdel.8
/usr/share/man/zh_TW/man8/groupmod.8
/usr/share/man/zh_TW/man8/useradd.8
/usr/share/man/zh_TW/man8/userdel.8
/usr/share/man/zh_TW/man8/usermod.8

%files locales -f shadow.lang
%defattr(-,root,root,-)

