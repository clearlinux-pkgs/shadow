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

install -d %{buildroot}%{_datadir}/pam.d/
install -m 0644 pam.d/* %{buildroot}%{_datadir}/pam.d/

# Handle link properly after rename, otherwise missing files would
# lead rpm failed dependencies.
ln -sf newgrp %{buildroot}%{_bindir}/sg

# util-linux provides /usr/bin/su
rm %{buildroot}%{_bindir}/su
rm %{buildroot}%{_datadir}/pam.d/su
find %{buildroot} -type f -name 'su.1' -exec rm {} \;

%find_lang %{name}

%files
%{_bindir}/groups
%{_bindir}/login
%{_bindir}/chfn
%{_bindir}/chsh
%{_bindir}/newgrp
%{_bindir}/passwd
%{_bindir}/newgidmap
%{_bindir}/newuidmap
%{_bindir}/chpasswd
%{_bindir}/vigr
%{_bindir}/vipw
%{_datadir}/pam.d/chage
%{_datadir}/pam.d/chfn
%{_datadir}/pam.d/chgpasswd
%{_datadir}/pam.d/chpasswd
%{_datadir}/pam.d/chsh
%{_datadir}/pam.d/groupadd
%{_datadir}/pam.d/groupdel
%{_datadir}/pam.d/groupmems
%{_datadir}/pam.d/groupmod
%{_datadir}/pam.d/newusers
%exclude %{_datadir}/pam.d/login
%{_datadir}/pam.d/passwd
%{_datadir}/pam.d/useradd
%{_datadir}/pam.d/userdel
%{_datadir}/pam.d/usermod
%{_bindir}/chage
%{_bindir}/expiry
%{_bindir}/faillog
%{_bindir}/gpasswd
%{_bindir}/lastlog
%{_bindir}/sg
%{_bindir}/chgpasswd
%{_bindir}/groupadd
%{_bindir}/groupdel
%{_bindir}/groupmems
%{_bindir}/groupmod
%{_bindir}/grpck
%{_bindir}/grpconv
%{_bindir}/grpunconv
%{_bindir}/logoutd
%{_bindir}/newusers
%{_bindir}/pwck
%{_bindir}/pwconv
%{_bindir}/pwunconv
%{_bindir}/useradd
%{_bindir}/userdel
%{_bindir}/usermod
%{_bindir}/nologin

%files -n shadow-doc
%{_mandir}/cs/
%{_mandir}/de/
%{_mandir}/da/
%{_mandir}/fi/
%{_mandir}/fr/
%{_mandir}/hu/
%{_mandir}/id/
%{_mandir}/it/
%{_mandir}/ja/
%{_mandir}/ko/
%{_mandir}/pl/
%{_mandir}/pt_BR/
%{_mandir}/ru/
%{_mandir}/sv/
%{_mandir}/tr/
%{_mandir}/zh_CN/
%{_mandir}/zh_TW/
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_mandir}/man5/*
%{_mandir}/man8/*

%files -n shadow-locale -f %{name}.lang
