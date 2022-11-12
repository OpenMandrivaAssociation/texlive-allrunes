Name:		texlive-allrunes
Version:	42221
Release:	1
Summary:	Fonts and LaTeX package for almost all runes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/allrunes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/allrunes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/allrunes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/allrunes.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This large collection of fonts (in Adobe Type 1 format), with
the LaTeX package gives access to almost all runes ever used in
Europe. The bundle covers not only the main forms but also a
lot of varieties.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/allrunes
%{_texmfdistdir}/fonts/source/public/allrunes
%{_texmfdistdir}/fonts/type1/public/allrunes
%{_texmfdistdir}/tex/latex/allrunes
%doc %{_texmfdistdir}/doc/fonts/allrunes
#- source
%doc %{_texmfdistdir}/source/fonts/allrunes

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
