Name:           shadow
Version:        4.5
Release:        46
License:        BSD-3-Clause Artistic-1.0
Summary:        Tools to change and administer password and group data
Url:            http://pkg-shadow.alioth.debian.org
Group:          base utils
Source0:        https://github.com/shadow-maint/shadow/releases/download/4.5/shadow-4.5.tar.xz
Source1:        chfn
Source2:        chpasswd
Source3:        chsh
Source5:        newusers
Source6:        passwd
BuildRequires:  Linux-PAM-dev
BuildRequires:  attr-dev
BuildRequires:  acl-dev
BuildRequires:	gdb

Patch1:         0001-Make-usermod-read-altfiles.patch
Patch2:         0002-Allow-lower-case-n-for-no-group.patch
Patch3:         0003-shadow-stateless-config.patch
Patch4:         0004-Use-correct-pam.d-path.patch
Patch5:         0005-Enable-stateless-login.patch
Patch6:         0006-Enable-statless-useradd-command.patch
Patch7:         0007-Enable-statless-gpasswd.patch
Patch8:         0008-Enable-stateless-usermod-command.patch
Patch9:         0009-Stateless-files-might-not-exist-in-etc.patch
Patch10:        0010-Make-glibc-give-up-memory-we-have-already-released.patch

%description
Tools to change and administer password and group data.

%package -n shadow-doc
Summary:        Tools to change and administer password and group data
Group:          doc

%description -n shadow-doc
Tools to change and administer password and group data.

%package -n shadow-locale
Summary:        Tools to change and administer password and group data
Group:          libs

%description -n shadow-locale
Tools to change and administer password and group data.

%prep
%setup -q
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

%build
export CFLAGS="$CFLAGS -Os -ffunction-sections"
%reconfigure --without-audit \
 --without-libcrack \
 --without-selinux \
 --enable-nls \
 --disable-rpath \
 --with-libpam \
 --with-acl \
 --with-attr \
 --sysconfdir=%{_sysconfdir}

make %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
%make_install

# Install pam.d stuff
mkdir pam.d
install %{SOURCE1} pam.d/
install %{SOURCE2} pam.d/
install %{SOURCE3} pam.d/
install %{SOURCE5} pam.d/
install %{SOURCE6} pam.d/

# Defaults are compiled in
rm -f %{buildroot}%{_sysconfdir}/default/useradd
rm -f %{buildroot}%{_sysconfdir}/login.defs

install -d %{buildroot}/usr/share/pam.d/
install -m 0644 pam.d/* %{buildroot}/usr/share/pam.d/

# Handle link properly after rename, otherwise missing files would
# lead rpm failed dependencies.
ln -sf newgrp %{buildroot}/usr/bin/sg

# util-linux provides /usr/bin/su
rm %{buildroot}/usr/bin/su
rm %{buildroot}/usr/share/pam.d/su
find %{buildroot} -type f -name 'su.1' -exec rm {} \;

%find_lang %{name}

%files
/usr/bin/groups
/usr/bin/login
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/passwd
/usr/bin/newgidmap
/usr/bin/newuidmap
/usr/bin/chpasswd
/usr/bin/vigr
/usr/bin/vipw
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
%exclude /usr/share/pam.d/login
/usr/share/pam.d/passwd
/usr/share/pam.d/useradd
/usr/share/pam.d/userdel
/usr/share/pam.d/usermod
/usr/bin/chage
/usr/bin/expiry
/usr/bin/faillog
/usr/bin/gpasswd
/usr/bin/lastlog
/usr/bin/sg
/usr/bin/chgpasswd
/usr/bin/groupadd
/usr/bin/groupdel
/usr/bin/groupmems
/usr/bin/groupmod
/usr/bin/grpck
/usr/bin/grpconv
/usr/bin/grpunconv
/usr/bin/logoutd
/usr/bin/newusers
/usr/bin/pwck
/usr/bin/pwconv
/usr/bin/pwunconv
/usr/bin/useradd
/usr/bin/userdel
/usr/bin/usermod
/usr/bin/nologin

%files -n shadow-doc
/usr/share/man/cs/
/usr/share/man/de/
/usr/share/man/da/
/usr/share/man/fi/
/usr/share/man/fr/
/usr/share/man/hu/
/usr/share/man/id/
/usr/share/man/it/
/usr/share/man/ja/
/usr/share/man/ko/
/usr/share/man/pl/
/usr/share/man/pt_BR/
/usr/share/man/ru/
/usr/share/man/sv/
/usr/share/man/tr/
/usr/share/man/zh_CN/
/usr/share/man/zh_TW/
/usr/share/man/man1/*
/usr/share/man/man3/*
/usr/share/man/man5/*
/usr/share/man/man8/*

%files -n shadow-locale -f %{name}.lang
