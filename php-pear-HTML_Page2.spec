%define     _class          HTML
%define     _subclass       Page2
%define		upstream_name	%{_class}_%{_subclass}
%define		pre		        beta

Name:		php-pear-%{upstream_name}
Version:	0.5.0
Release:	11
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

cd %{upstream_name}-%{version}%{pre}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}%{pre}/examples
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml




%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-10mdv2012.0
+ Revision: 741995
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-9
+ Revision: 679346
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-8mdv2011.0
+ Revision: 613672
- the mass rebuild of 2010.1 packages

* Sat Dec 12 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.5.0-7mdv2010.1
+ Revision: 477868
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.5.0-6mdv2010.0
+ Revision: 441119
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-5mdv2009.1
+ Revision: 322114
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-4mdv2009.0
+ Revision: 236873
- rebuild

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 0.5.0-3mdv2008.1
+ Revision: 171039
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake
- fix description-line-too-long
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-2mdv2007.0
+ Revision: 81631
- Import php-pear-HTML_Page2

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-2mdk
- new group (Development/PHP)

* Mon Nov 07 2005 Oden Eriksson <oeriksson@mandriva.com> 0.5.0-1mdk
- initial Mandriva package

