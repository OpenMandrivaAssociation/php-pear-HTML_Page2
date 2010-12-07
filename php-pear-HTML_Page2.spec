%define     _class          HTML
%define     _subclass       Page2
%define		upstream_name	%{_class}_%{_subclass}
%define		pre		        beta

Name:		php-pear-%{upstream_name}
Version:	0.5.0
Release:	%mkrel 8
Summary:	Base class for XHTML page generation
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/HTML_Page2/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}%{pre}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The PEAR::HTML_Page2 package provides a simple interface for generating an
XHTML compliant page.
* supports virtually all HTML doctypes, from HTML 2.0 through XHTML 1.1 and
XHTML Basic 1.0
  plus preliminary support for XHTML 2.0
* namespace support
* global language declaration for the document
* line ending styles
* full META tag support
* support for stylesheet declaration in the head section
* support for script declaration in the head section
* support for linked stylesheets and scripts
* full support for header link tags
* body can be a string, object with toHtml or toString methods or an array (can
be combined)

Ideas for use:
* Use to validate the output of a class for XHTML compliance
* Quick prototyping using PEAR packages is now a breeze

This class has in PEAR status: %{_status}.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}%{pre}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}%{pre}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


