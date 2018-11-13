%if 0%{?_version:1}
%define         _verstr      %{_version}
%else
%define         _verstr      0.0.1
%endif

Name:       azure_metrics_exporter
Version:        %{_verstr}
Release:        1%{?dist}
Summary:    Azure Metrics Exporter
License:    FIXME

%description
 Azure Metrics Exporter
 
%prep
# we have no source, so nothing here

%build

%install
mkdir -p %{buildroot}/usr/bin/
install -m 755 azure_metrics_exporter %{buildroot}/usr/bin/azure_metrics_exporter

%files
/usr/bin/azure_metrics_exporter

%changelog
# let skip this for now
