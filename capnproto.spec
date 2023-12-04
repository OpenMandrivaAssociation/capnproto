%define libname %mklibname capnp
%define devname %mklibname -d capnp

Name: capnproto
Version: 1.0.1.1
Release: 1
Summary: C++ library and tools for a serialization/RPC system
Group: System/Libraries
License: MIT
Url: http://capnproto.org/
Source0: https://github.com/capnproto/capnproto/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: ninja
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(openssl)

%description
C++ library and tools for a serialization/RPC system

%package -n %{libname}
Summary: C++ library and tools for a serialization/RPC system
Group: System/Libraries

%description -n %{libname}
C++ library and tools for a serialization/RPC system

%files -n %{libname}
%{_libdir}/libcapnp.so*
%{_libdir}/libcapnpc.so*
%{_libdir}/libcapnp-rpc.so*
%{_libdir}/libcapnp-json.so*
%{_libdir}/libcapnp-websocket.so*
%{_libdir}/libkj.so*
%{_libdir}/libkj-async.so*
%{_libdir}/libkj-gzip.so*
%{_libdir}/libkj-http.so*
%{_libdir}/libkj-test.so*
%{_libdir}/libkj-tls.so*

%package -n %{devname}
Summary: Development files for C++ library and tools for a serialization/RPC system
Group: Development/C++ and C
Requires: %{libname} = %{EVRD}
Requires: %{name} = %{EVRD}

%description -n %{devname}
Development files for C++ library and tools for a serialization/RPC system

%files -n %{devname}
%{_includedir}/capnp
%{_includedir}/kj
%{_libdir}/cmake/CapnProto
%{_libdir}/pkgconfig/*.pc

%files
%{_bindir}/capnp*

%prep
%autosetup -p1
%cmake_kde5

%build
# FIXME this is not exactly cross-compilation friendly...
# but capnproto likes using its own tools
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:"$(pwd)/build/c++/src/capnp":"$(pwd)/build/c++/src/kj"
%ninja_build -C build

%install
%ninja_install -C build
