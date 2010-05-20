%define		php_min_version 5.0.0
%define		pkgname	jsmin
%include	/usr/lib/rpm/macros.php
Summary:	PHP implementation of Douglas Crockford's JSMin
Name:		php-%{pkgname}
Version:	1.1.1
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://github.com/rgrove/jsmin-php/tarball/master?/%{pkgname}.tgz
# Source0-md5:	1065a82d2d9f76e46ab74dd545c5fdb6
URL:		http://github.com/rgrove/jsmin-php/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed	>=4.0
Requires:	php-common >= 4:%{php_min_version}
Requires:	php-pcre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP implementation of Douglas Crockford's JSMin.

%prep
%setup -qc
mv *-jsmin-php-*/* .
%undos *.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_data_dir}
cp -a jsmin.php $RPM_BUILD_ROOT%{php_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_data_dir}/jsmin.php
