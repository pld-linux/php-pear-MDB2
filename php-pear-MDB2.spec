%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_pearname	%{_class}
%define		_status		stable
Summary:	%{_pearname} - unified database API
Summary(pl.UTF-8):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	2.3.0
Release:	1
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	31c7294943b665c293f1453e1c4b20a4
URL:		http://pear.php.net/package/MDB2/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.3.0
Requires:	php-pear
Requires:	php-pear-PEAR-core >= 1:1.4.0-0.b1
Requires:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# (probably) included in tests
%define		_noautoreq 'pear(Console_TestListener.php)' 'pear(HTML_TestListener.php)' 'pear(XML/DTD/XmlValidator.php)' 'pear(testUtils.php)' 'pear(test_setup.php)'

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

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver/Native

%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
