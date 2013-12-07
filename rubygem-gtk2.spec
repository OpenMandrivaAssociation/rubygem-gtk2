# Generated from pkg-config-1.1.4.gem by gem2rpm5 -*- rpm-spec -*-
%define	rbname	gtk2

Summary:	Ruby binding of GTK+-2.x
Name:		rubygem-%{rbname}

Version:	1.1.5
Release:	5
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://ruby-gnome2.sourceforge.jp/
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildRequires:  rubygem(gdk_pixbuf2)
BuildRequires:  rubygem(atk)
BuildRequires:  rubygem(pango)
BuildRequires:  rubygem-atk-devel
BuildRequires:  rubygem-glib2-devel
BuildRequires:  rubygem-pango-devel
BuildRequires:  ruby-devel
BuildRequires:  pkgconfig(gtk+-2.0)
Obsoletes:      ruby-gtk2

%description
Ruby binding of GTK-2.x.

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description	doc
Documents, RDoc & RI documentation for %{name}.

%package    devel                                                                                                                                                                                              
Summary:    Development files for %{name}
Group:      Development/Ruby

%description	devel
Development files for %{name}.

%prep
%setup -q

%build
%gem_build

%install
%gem_install

%files
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/*.rb
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/%{rbname}/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/%{rbname}.so

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

%files devel
%{ruby_sitearchdir}/*.h


%changelog

