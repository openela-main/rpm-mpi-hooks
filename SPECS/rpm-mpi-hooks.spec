Name:           rpm-mpi-hooks
Version:        8
Release:        2%{?dist}
Summary:        RPM dependency generator hooks for MPI packages

License:        MIT
BuildArch:      noarch

Source0:        mpi.attr
Source1:        mpilibsymlink.attr
Source2:        mpi.prov
Source3:        mpi.req
Source4:        LICENSE

Requires:       filesystem
# Instead of adding a BuildRequires to every MPI implementation spec
Requires:       environment(modules)

%description
RPM dependency generator hooks for MPI packages. This package should be added
as a BuildRequires to all mpi implementations (i.e. openmpi, mpich) as well as
a Requires to the their -devel packages.


%prep
cp -a %SOURCE4 .


%build
# Nothing to build


%install
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/fileattrs/mpi.attr
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/mpilibsymlink.attr
install -Dpm 0755 %{SOURCE2} %{buildroot}%{_rpmconfigdir}/mpi.prov
install -Dpm 0755 %{SOURCE3} %{buildroot}%{_rpmconfigdir}/mpi.req


%files
%license LICENSE
%{_rpmconfigdir}/fileattrs/mpi.attr
%{_rpmconfigdir}/fileattrs/mpilibsymlink.attr
%{_rpmconfigdir}/mpi.req
%{_rpmconfigdir}/mpi.prov


%changelog
* Tue May 18 2021 Honggang Li <honli@redhat.com> - 8-2
- Rebuilt after building tool chain update
- Resolves: rhbz#1924665

* Wed Apr 07 2021 Honggang Li <honli@redhat.com> - 8-1
- Sync with latest Fedora repo
- Resolves: rhbz#1924665

* Thu Sep 13 2018 Jarod Wilson <jarod@redhat.com> - 5-4
- Make hooks more resilient to missing info
- Error out with a useful message when necessary info isn't there
- Resolves: rhbz#1627122

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Apr 17 2017 Orion Poplawski <orion@cora.nwra.com> - 5-1
- Exclude build-id files from symlink requires path (bug #1435690)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 12 2016 Sandro Mani <manisandro@gmail.com> 4-1
- Use RPM_BUILD_ROOT directly instead of passing it as an argument
- Use MPI_PYTHON3_SITEARCH

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jan 08 2016 Sandro Mani <manisandro@gmail.com> 3-5
- Add quotes around strings which may contain spaces

* Tue Dec 22 2015 Orion Poplawski <orion@cora.nwra.com> - 3-4
- Require environment(modules)

* Mon Nov 2 2015 Orion Poplawski <orion@cora.nwra.com> - 3-3
- Drop requires rpm-build, fileattrs now owned by rpm

* Mon Aug 17 2015 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3-2
- Also handle modules for Python 3

* Mon Aug 10 2015 Sandro Mani <manisandro@gmail.com> 3-1
- Also handle binaries in $MPI_FORTRAN_MOD_DIR and $MPI_PYTHON_SITEARCH

* Sun Jul 26 2015 Sandro Mani <manisandro@gmail.com> 2-1
- Add %%__mpi_magic, %%__mpi_flags to mpi.attrs
- Add mpilibsymlink.attr

* Thu Jul 09 2015 Sandro Mani <manisandro@gmail.com> 1.0-4
- mpi.prov, mpi.req: Use "module -t avail" instead of "module avail"
- mpi.prov, mpi.req: Also look in moduledirs in %%buildroot
- mpi.attrs: add %%__libsymlink_exclude_path

* Thu Jul 09 2015 Sandro Mani <manisandro@gmail.com> 1.0-3
- Add LICENSE

* Thu Jul 09 2015 Sandro Mani <manisandro@gmail.com> 1.0-2
- BuildRequires: rpm -> rpm-build
- Change license to MIT

* Thu Jul 09 2015 Sandro Mani <manisandro@gmail.com> 1.0-1
- Initial package
