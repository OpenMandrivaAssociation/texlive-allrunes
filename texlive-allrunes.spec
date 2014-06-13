# revision 21886
# category Package
# catalog-ctan /fonts/allrunes
# catalog-date 2007-01-14 10:14:42 +0100
# catalog-license lppl
# catalog-version 2.1
Name:		texlive-allrunes
Version:	2.1
Release:	7
Summary:	Fonts and LaTeX package for almost all runes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/allrunes
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/allrunes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/allrunes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/allrunes.source.tar.xz
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
%{_texmfdistdir}/fonts/map/dvips/allrunes/allrunes.map
%{_texmfdistdir}/fonts/source/public/allrunes/frua.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruabm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruabn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruabq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruabr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruabs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruabt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruacm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruacn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruacq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruacr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruacs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruact.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruakm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruakn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruakq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruakr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruaks.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruakt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frualm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frualn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frualq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frualr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruals.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frualt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruamm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruamn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruamq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruamr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruams.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruamt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruanm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruann.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruanq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruanr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruans.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruant.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frubase.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruc.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucbm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucbn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucbq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucbr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucbs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucbt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruccm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruccn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruccq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruccr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruccs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucct.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruckm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruckn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruckq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruckr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucks.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruckt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruclm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucln.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruclq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruclr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucls.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruclt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucmm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucmn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucmq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucmr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucms.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucmt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucnm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucnn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucnq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucnr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucns.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frucnt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frul.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulbm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulbn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulbq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulbr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulbs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulbt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulcm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulcn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulcq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulcr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulcs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulct.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulkm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulkn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulkq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulkr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulks.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulkt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frullm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulln.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frullq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frullr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulls.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frullt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulmm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulmn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulmq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulmr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulms.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulmt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulnm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulnn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulnq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulnr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulns.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frulnt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frum.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumbm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumbn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumbq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumbr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumbs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumbt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumcm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumcn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumcq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumcr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumcs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumct.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumkm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumkn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumkq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumkr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumks.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumkt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumlm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumln.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumlq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumlr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumls.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumlt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frummm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frummn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frummq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frummr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumms.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frummt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumnm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumnn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumnq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumnr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumns.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frumnt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frun.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunbm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunbn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunbq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunbr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunbs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunbt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruncm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruncn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruncq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruncr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/fruncs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunct.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunkm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunkn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunkq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunkr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunks.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunkt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunlm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunln.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunlq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunlr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunls.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunlt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunmm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunmn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunmq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunmr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunms.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunmt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunnm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunnn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunnq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunnr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunns.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frunnt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frusep.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frut.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutbm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutbn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutbq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutbr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutbs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutbt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutcm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutcn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutcq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutcr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutcs.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutct.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutkm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutkn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutkq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutkr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutks.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutkt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutlm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutln.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutlq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutlr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutls.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutlt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutmm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutmn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutmq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutmr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutms.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutmt.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutnm.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutnn.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutnq.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutnr.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutns.mf
%{_texmfdistdir}/fonts/source/public/allrunes/frutnt.mf
%{_texmfdistdir}/fonts/type1/public/allrunes/fruabm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruabn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruabq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruabr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruabs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruabt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruacm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruacn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruacq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruacr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruacs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruact.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruakm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruakn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruakq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruakr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruaks.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruakt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frualm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frualn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frualq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frualr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruals.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frualt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruamm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruamn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruamq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruamr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruams.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruamt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruanm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruann.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruanq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruanr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruans.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruant.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucbm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucbn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucbq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucbr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucbs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucbt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruccm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruccn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruccq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruccr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruccs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucct.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruckm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruckn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruckq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruckr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucks.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruckt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruclm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucln.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruclq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruclr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucls.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruclt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucmm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucmn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucmq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucmr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucms.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucmt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucnm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucnn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucnq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucnr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucns.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frucnt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulbm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulbn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulbq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulbr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulbs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulbt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulcm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulcn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulcq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulcr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulcs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulct.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulkm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulkn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulkq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulkr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulks.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulkt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frullm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulln.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frullq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frullr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulls.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frullt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulmm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulmn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulmq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulmr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulms.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulmt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulnm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulnn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulnq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulnr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulns.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frulnt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumbm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumbn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumbq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumbr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumbs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumbt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumcm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumcn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumcq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumcr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumcs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumct.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumkm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumkn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumkq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumkr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumks.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumkt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumlm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumln.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumlq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumlr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumls.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumlt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frummm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frummn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frummq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frummr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumms.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frummt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumnm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumnn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumnq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumnr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumns.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frumnt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunbm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunbn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunbq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunbr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunbs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunbt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruncm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruncn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruncq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruncr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/fruncs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunct.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunkm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunkn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunkq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunkr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunks.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunkt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunlm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunln.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunlq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunlr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunls.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunlt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunmm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunmn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunmq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunmr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunms.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunmt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunnm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunnn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunnq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunnr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunns.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frunnt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutbm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutbn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutbq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutbr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutbs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutbt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutcm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutcn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutcq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutcr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutcs.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutct.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutkm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutkn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutkq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutkr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutks.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutkt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutlm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutln.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutlq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutlr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutls.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutlt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutmm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutmn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutmq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutmr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutms.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutmt.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutnm.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutnn.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutnq.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutnr.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutns.pfb
%{_texmfdistdir}/fonts/type1/public/allrunes/frutnt.pfb
%{_texmfdistdir}/tex/latex/allrunes/allrunes.sty
%{_texmfdistdir}/tex/latex/allrunes/ara.fd
%{_texmfdistdir}/tex/latex/allrunes/arc.fd
%{_texmfdistdir}/tex/latex/allrunes/arl.fd
%{_texmfdistdir}/tex/latex/allrunes/arm.fd
%{_texmfdistdir}/tex/latex/allrunes/arn.fd
%{_texmfdistdir}/tex/latex/allrunes/art.fd
%doc %{_texmfdistdir}/doc/fonts/allrunes/README
%doc %{_texmfdistdir}/doc/fonts/allrunes/allrunes.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/allrunes/allrunes.dtx
%doc %{_texmfdistdir}/source/fonts/allrunes/allrunes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 2.1-2
+ Revision: 749162
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 2.1-1
+ Revision: 717814
- texlive-allrunes
- texlive-allrunes
- texlive-allrunes
- texlive-allrunes
- texlive-allrunes

