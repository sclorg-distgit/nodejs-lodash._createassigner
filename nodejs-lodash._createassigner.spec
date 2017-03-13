%{?scl:%scl_package nodejs-lodash._createassigner}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-lodash._createassigner

%global npm_name lodash._createassigner
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-lodash._createassigner
Version:	3.1.1
Release:	4%{?dist}
Summary:	The modern build of lodash’s internal `createAssigner` as a module.
Url:		https://lodash.com/
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
%endif

Requires:	%{?scl_prefix}npm(lodash._bindcallback)
Requires:	%{?scl_prefix}npm(lodash._isiterateecall)
Requires:	%{?scl_prefix}npm(lodash.restparam)

%description
The modern build of lodash’s internal `createAssigner` as a module.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{!?_licensedir:%global license %doc}
%{nodejs_sitelib}/lodash._createassigner

%doc README.md
%doc LICENSE.txt

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.1-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.1.1-3
- Rebuilt with updated metapackage

* Wed Jan 13 2016 Tomas Hrcka <thrcka@redhat.com> - 3.1.1-2
- Enable scl macros

* Wed Jan 13 2016 Tomas Hrcka <thrcka@redhat.com> - 3.1.1-1
- Initial build
