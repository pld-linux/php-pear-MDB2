%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_pearname	%{_class}
%define		_status		beta

Summary:	%{_pearname} - unified database API
Summary(pl):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	2.0.0
%define	_pre	beta5
%define	_rel	1
Release:	0.%{_pre}.%{_rel}
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_pre}.tgz
# Source0-md5:	647f695efebee5b805e3e4ec5c3840bc
URL:		http://pear.php.net/package/MDB2/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-PEAR >= 1:1.0b1
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

%description -l pl
MDB2 to połączenie PEAR DB i Metabases, które daje ujednolicone API do
baz danych. Zawiera także metody zapewniające przenośność i emulację
właściwości dla baz danych. Najważniejsza cecha to niezależny od bazy
danych zarządca schematów XML.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
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
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
