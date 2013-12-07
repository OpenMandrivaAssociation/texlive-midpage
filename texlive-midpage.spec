# revision 17484
# category Package
# catalog-ctan /macros/latex/contrib/midpage
# catalog-date 2010-03-17 12:20:59 +0100
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-midpage
Version:	1.1a
Release:	6
Summary:	Environment for vertical centring
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/midpage
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midpage.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/midpage.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The environment will centre text, if immediately preceded and
followed by \clearpage.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/midpage/midpage.sty
%doc %{_texmfdistdir}/doc/latex/midpage/midpage.pdf
%doc %{_texmfdistdir}/doc/latex/midpage/midpage.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-2
+ Revision: 753985
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1a-1
+ Revision: 719031
- texlive-midpage
- texlive-midpage
- texlive-midpage
- texlive-midpage

