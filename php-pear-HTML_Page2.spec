%define         _class          HTML
%define         _subclass       Page2
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
%define		_ver		%{version}beta

Summary:	Base class for XHTML page generation
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	%mkrel 5
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{_ver}.tar.bz2
URL:		http://pear.php.net/package/HTML_Page2/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install %{_pearname}-%{_ver}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{_ver}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{_ver}/examples
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


