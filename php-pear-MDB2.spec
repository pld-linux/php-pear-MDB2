%include	/usr/lib/rpm/macros.php
%define		_pearname	MDB2
%define		_status		beta
%define		subver	b3
%define		rel		3
Summary:	%{_pearname} - unified database API
Summary(pl.UTF-8):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	2.5.0
Release:	0.%{subver}.%{rel}
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	5a4333a18f331a5176010ad45f9617ea
URL:		http://pear.php.net/package/MDB2/
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.3.6
Requires:	php-pear-XML_Parser
Obsoletes:	php-pear-MDB2-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# (probably) included in tests
%define		_noautoreq pear(Console_TestListener.php) pear(HTML_TestListener.php) pear(XML/DTD/XmlValidator.php) pear(testUtils.php) pear(test_setup.php)

%description
MDB2 is a merge of PEAR's DB and Metabases that provides a unified DB
API. It also provides methods for DB portability and DB feature
emulation. Most notably it features a DB independent XML-Schema
manager.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
MDB2 to połączenie PEAR DB i Metabases, które daje ujednolicone API do
baz danych. Zawiera także metody zapewniające przenośność i emulację
właściwości dla baz danych. Najważniejsza cecha to niezależny od bazy
danych zarządca schematów XML.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_examplesdir}/%{name}-%{version}}
install -d $RPM_BUILD_ROOT%{php_pear_dir}/MDB2/Driver/Native
%pear_package_install

rm -f $RPM_BUILD_ROOT%{php_pear_dir}/data/MDB2/LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/MDB2

%{_examplesdir}/%{name}-%{version}
