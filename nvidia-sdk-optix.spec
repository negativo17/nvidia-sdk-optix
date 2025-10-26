Name:           nvidia-sdk-optix
Version:        9.0.0
Release:        1%{?dist}
Summary:        NVIDIA OptiX Ray Tracing Engine APIs
License:        https://developer.download.nvidia.com/designworks/DesignWorks_SDKs_Samples_Tools_License_distrib_use_rights_2017_06_13.pdf
URL:            https://developer.nvidia.com/optix
BuildArch:      noarch

# We're packaging only the headers, so the first run file is enough:
Source0:        NVIDIA-OptiX-SDK-%{version}-linux64-x86_64.sh
Source1:        NVIDIA-OptiX-SDK-%{version}-linux64-aarch64.sh

%description
An application framework for achieving optimal ray tracing performance on the
GPU. It provides a simple, recursive, and flexible pipeline for accelerating ray
tracing algorithms. Bring the power of NVIDIA GPUs to your ray tracing
applications with programmable intersection, ray generation, and shading.

%package samples
Summary:        NVIDIA OptiX Sample application source code
Requires:       %{name} = %{?epoch}:%{version}-%{release}

%description samples
This package contains sample application source code demonstrating various
encoding and decoding capabilities.

%prep
%setup -c -T
sh %{SOURCE0} --skip-license --prefix=`pwd`

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_includedir}/optix
cp -fra include/* %{buildroot}%{_includedir}/optix/

%files
%license OptiX_EndUserLicense.pdf OptiX_ThirdParty_Licenses.txt
%doc doc/OptiX_API_Reference_%{version}.pdf doc/OptiX_Programming_Guide_%{version}.pdf
%{_includedir}/optix

%files samples
%doc SDK/*

%changelog
* Sun Oct 26 2025 Simone Caronni <negativo17@gmail.com> - 9.0.0-1
- Update to 9.0.0.

* Mon Jan 27 2025 Simone Caronni <negativo17@gmail.com> - 8.1.0-1
- Update to 8.1.0.

* Thu Sep 28 2023 Simone Caronni <negativo17@gmail.com> - 8.0.0-1
- Update to 8.0.0.

* Fri Oct 07 2022 Simone Caronni <negativo17@gmail.com> - 7.5.0-1
- Update to 7.5.0.

* Wed Sep 22 2021 Simone Caronni <negativo17@gmail.com> - 7.3.0-1
- Update to 7.3.0.

* Tue Aug 25 2020 Simone Caronni <negativo17@gmail.com> - 7.1.0-1
- First build.
