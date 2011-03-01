%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	CSV_DataSource
%define		_status		stable
%define		_pearname	File_CSV_DataSource
Summary:	%{_pearname} - CSV-file data extraction tool
Summary(pl.UTF-8):	%{_pearname} - wydobywanie danych w formacie CSV
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	3
License:	MIT
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	3a88a49d33d26f9d9f4a5dfcf7531ea0
URL:		http://pear.php.net/package/File_CSV_DataSource/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-File_CSV_DataSource-tests
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
