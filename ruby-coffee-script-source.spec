%define pkgname coffee-script-source
Summary:	CoffeeScript is a little language that compiles into JavaScript
Name:		ruby-%{pkgname}
Version:	1.8.0
Release:	2
License:	Ruby-alike
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	7bc7b4d2a44234cd558e928c1f1dc5d2
URL:		http://rubygems.org/gems/jquery-rails
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %(locale -a | grep -q '^en_US$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Underneath all of those embarrassing braces and semicolons, JavaScript
has always had a gorgeous object model at its heart. CoffeeScript is
an attempt to expose the good parts of JavaScript in a simple way.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec

# UTF8 locale needed for doc generation
export LC_ALL=en_US.UTF-8
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid
rm ri/cache.ri
#rm -r ri/{Class,Date,DateTime}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir},%{ruby_ridir},%{ruby_rdocdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{pkgname}-%{version}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/coffee_script
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{pkgname}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/CoffeeScript
