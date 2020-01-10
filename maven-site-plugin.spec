Name:           maven-site-plugin
Version:        3.2
Release:        7%{?dist}
Summary:        Maven Site Plugin

Group:          Development/Libraries
License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-site-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{name}/%{version}/%{name}-%{version}-source-release.zip

Patch0:         0001-Port-to-jetty-9.patch
Patch1:         0001-Fix-jetty-dependencies.patch
# Jetty is needed only in interactive mode of maven-site-plugin. Change
# dependency scope from compile to provided to reduce dependency bloat.
Patch2:         %{name}-jetty-provided.patch

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: maven-local
BuildRequires: maven-artifact-manager
BuildRequires: maven-plugin-plugin
BuildRequires: maven-assembly-plugin
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-doxia-sink-api
BuildRequires: maven-doxia-logging-api
BuildRequires: maven-doxia-core
BuildRequires: maven-doxia-module-xhtml
BuildRequires: maven-doxia-module-apt
BuildRequires: maven-doxia-module-xdoc
BuildRequires: maven-doxia-module-fml
BuildRequires: maven-doxia-sitetools
BuildRequires: maven-doxia-tools >= 1.4-8
BuildRequires: maven-project
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-shade-plugin
BuildRequires: maven-plugin-testing-harness
BuildRequires: maven-wagon
BuildRequires: maven-reporting-exec
BuildRequires: plexus-containers-component-metadata
BuildRequires: jetty-client >= 9.0.0-0.1.RC0
BuildRequires: jetty-server >= 9.0.0-0.1.RC0
BuildRequires: jetty-servlet >= 9.0.0-0.1.RC0
BuildRequires: jetty-util >= 9.0.0-0.1.RC0
BuildRequires: jetty-webapp >= 9.0.0-0.1.RC0
BuildRequires: servlet3
BuildRequires: plexus-archiver
BuildRequires: plexus-containers-container-default
BuildRequires: plexus-i18n
BuildRequires: plexus-velocity
BuildRequires: plexus-utils
BuildRequires: jetty-parent

Provides:       maven2-plugin-site = %{version}-%{release}
Obsoletes:      maven2-plugin-site <= 0:2.0.8

%description
The Maven Site Plugin is a plugin that generates a site for the current project.

%package javadoc
Group:          Documentation
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2

%build
# skipping tests because we need to fix them first for jetty update
%mvn_build -f

%install
%mvn_install

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 3.2-7
- Mass rebuild 2013-12-27

* Wed Nov 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-6
- Remove BR on main jetty package

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Fri Mar  1 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-4
- Merge branch 'port-to-jetty-9' into master

* Tue Feb 26 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-3
- Change jetty dependency scope to provided

* Mon Feb 25 2013 Michal Srb <msrb@redhat.com> - 3.2-3
- Port to jetty 9.0.0

* Thu Feb 07 2013 Michal Srb <msrb@redhat.com> - 3.2-2
- Migrate from maven-doxia to doxia subpackages

* Thu Jan 24 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-1
- Update to upstream version 3.2
- Build with xmvn

* Tue Oct 30 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-3
- Don't require full jetty, only minimal set of subpackages

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jun 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-1
- Updatw to upstream 3.1

* Wed Apr 18 2012 Alexander Kurtakov <akurtako@redhat.com> 3.0-5
- BR/R servlet 3.

* Thu Jan 26 2012 Alexander Kurtakov <akurtako@redhat.com> 3.0-4
- Add BR/R on jetty-parent.

* Thu Jan 26 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 3.0-3
- Port for jetty 8.1.0
- Small spec cleanups

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Aug 12 2011 Alexander Kurtakov <akurtako@redhat.com> 3.0-1
- Update to upstream 3.0 release.

* Thu Jul 21 2011 Jaromir Capik <jcapik@redhat.com> - 2.3-3
- Removal of plexus-maven-plugin dependency (not needed)

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.3-2
- Add several missing things to (Build)Requires
- Fix build for maven3-only buildroot

* Wed May 25 2011 Alexander Kurtakov <akurtako@redhat.com> 2.3-1
- Update to new upstream version.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Alexander Kurtakov <akurtako@redhat.com> 2.2-1
- Update to new upstream version.

* Tue Jun 15 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1-3
- Requires maven-doxia-tools.

* Tue May 18 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1-2
- Fix requires.

* Tue May 18 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1-1
- Initial package.
