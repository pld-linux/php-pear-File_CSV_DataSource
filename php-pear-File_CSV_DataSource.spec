%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	CSV_DataSource
%define		_status		beta
%define		_pearname	File_CSV_DataSource
Summary:	%{_pearname} - CSV-file data extraction tool
Summary(pl.UTF-8):	%{_pearname} - wydobywanie danych w formacie CSV
Name:		php-pear-%{_pearname}
Version:	0.2.7
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	11fc31dbef561eb379de8561d49a85c2
URL:		http://pear.php.net/package/File_CSV_DataSource/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple data access object for CSV files in php5.

Takes the data from a CSV file and makes it accessable through a
client-interface.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Prosty obiektowy interfejs dostępu do plików CSV.

Klasa ta pobiera dane z pliku CSV i udostępnia je za pomocą interfejsu
klienckiego.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/File_CSV_DataSource/{docs/examples,docs/README}
%dir %{php_pear_dir}/File/CSV
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/CSV/DataSource.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/File_CSV_DataSource
