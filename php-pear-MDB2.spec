%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_pearname	%{_class}
%define		_status		beta

Summary:	%{_pearname} - unified database API
Summary(pl):	%{_pearname} - zunifikowane API baz danych
Name:		php-pear-%{_pearname}
Version:	2.0.0
%define	_pre	beta2
Release:	0.%{_pre}
Epoch:		1
License:	BSD style
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{_pre}.tgz
# Source0-md5:	202829a526d27207bc46823b3b5b8553
URL:		http://pear.php.net/package/MDB2/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{Driver/{Datatype,Manager,Native,Reverse},Tools}

install %{_pearname}-%{version}%{_pre}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/
install %{_pearname}-%{version}%{_pre}/%{_class}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}%{_pre}/%{_class}/Driver/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver/
install %{_pearname}-%{version}%{_pre}/%{_class}/Driver/Datatype/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver/Datatype/
install %{_pearname}-%{version}%{_pre}/%{_class}/Driver/Manager/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver/Manager/
install %{_pearname}-%{version}%{_pre}/%{_class}/Driver/Native/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver/Native/
install %{_pearname}-%{version}%{_pre}/%{_class}/Driver/Reverse/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Driver/Reverse/
install %{_pearname}-%{version}%{_pre}/%{_class}/Tools/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/Tools/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}%{_pre}/{docs/,tests/}
%{php_pear_dir}/*.php
%{php_pear_dir}/%{_class}
