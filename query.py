# Calculates the average number of running containers per pod within a specified time range.
queryFmtPods = 'avg(kube_pod_container_status_running{%s} != 0) by (pod, namespace)[%s:%s]'

# Calculates the average number of running containers per pod, including the unique identifier (UID) of the pod.
queryFmtPodsUID = 'avg(kube_pod_container_status_running{%s} != 0) by (pod, namespace, uid)[%s:%s]'

# Calculates the average memory allocated to containers over time.
# ///////////////////////////////////////////////////////////////
# queryFmtRAMBytesAllocated = 'avg(avg_over_time(container_memory_allocation_bytes{container!="", container!="POD", node!=""}[%s:%s])) by (%s, container, node, exported_instace)'
queryFmtRAMBytesAllocated  = 'avg_over_time(container_memory_allocation_bytes{container!="", container!="POD", node!=""}[%s])[%s:%s] '

# Calculates the average memory requested by containers over time.
queryFmtRAMRequests = 'avg(avg_over_time(kube_pod_container_resource_requests{resource="memory", unit="byte", container!="", container!="POD", node!=""}[%s:%s])) by (container, pod, namespace, node)'

# Calculates the average memory usage by containers over time.
# ///////////////////////////////////////////////////////////////
# queryFmtRAMUsageAvg = 'avg(avg_over_time(container_memory_working_set_bytes{container!="", container_name!="POD", container!="POD"}[%s:%s])) by (%s,ontainer,end_point,node,service)'
queryFmtRAMUsageAvg = 'avg_over_time(container_memory_working_set_bytes{container!="", container_name!="POD", container!="POD"}[%s])[%s:%s]'

# Finds the maximum memory usage by containers over time.
queryFmtRAMUsageMax = 'max(max_over_time(container_memory_working_set_bytes{container!="", container_name!="POD", container!="POD"}[%s:%s])) by (container_name, container, pod_name, pod, namespace, instance)'

# Calculates the average CPU cores allocated to containers over time.
# ///////////////////////////////////////////////////////////////
# queryFmtCPUCoresAllocated = 'avg(avg_over_time(container_cpu_allocation{container!="", container!="POD", node!=""}[%s:%s])) by (%s,container,exported_instance,job, node)'
queryFmtCPUCoresAllocated = 'avg_over_time(container_cpu_allocation{container!="", container!="POD", node!=""}[%s])[%s:%s]'

# Calculates the average CPU cores requested by containers over time.
queryFmtCPURequests = 'avg_over_time(kube_pod_container_resource_requests{resource="cpu", unit="core", container!="", container!="POD", node!=""}[%s])[%s:%s]'
 
# Calculates the average CPU usage by containers over time.
# ///////////////////////////////////////////////////////////////
queryFmtCPUUsageAvg = 'avg(rate(container_cpu_usage_seconds_total{container!="", container_name!="POD", container!="POD"}[%s:%s])) by (%s,endpoint,cpu,service,node, container)'
# queryFmtCPUUsageAvg = 'rate(container_cpu_usage_seconds_total{container!="", container_name!="POD", container!="POD"}[%s])) by (%s,endpoint,cpu,service,node, container)'


# Calculates the average GPU resources requested by containers over time.
queryFmtGPUsRequested = 'avg_over_time(kube_pod_container_resource_requests{resource="nvidia_com_gpu", container!="",container!="POD", node!=""}[%s])[%s:%s]'

# Calculates the average GPU usage by containers over time.
# ///////////////////////////////////////////////////////////////
# queryFmtGPUsUsageAvg = 'avg(avg_over_time(DCGM_FI_PROF_GR_ENGINE_ACTIVE{container!=""}[%s:%s])) by (%s,container,Hostname,GPU_I_ID,GPU_I_PROFILE,DCGM_FI_DRIVER_VERSION,gpu,device,job,modelName)'
queryFmtGPUsUsageAvg = 'avg_over_time(DCGM_FI_PROF_GR_ENGINE_ACTIVE{container!=""}[%s])[%s:%s]'


# Calculates the average GPU resources allocated to containers over time.
# ///////////////////////////////////////////////////////////////
# queryFmtGPUsAllocated = 'avg(avg_over_time(container_gpu_allocation{container!="", container!="POD", node!=""}[%s:%s])) by (%s,container,job,exported_instance,node)'
queryFmtGPUsAllocated = 'avg_over_time(container_gpu_allocation{container!="", container!="POD", node!=""}[%s])[%s:%s]'


# Calculates the average cost of CPU usage per hour for each node.
queryFmtNodeCostPerCPUHr = 'avg(avg_over_time(node_cpu_hourly_cost{%s}[%s:%s])) by (node, instance_type, provider_id)'

# Calculates the average cost of RAM usage per GiB per hour for each node.
queryFmtNodeCostPerRAMGiBHr = 'avg(avg_over_time(node_ram_hourly_cost{%s}[%s:%s])) by (node, instance_type, provider_id)'

# Calculates the average cost of GPU usage per hour for each node.
queryFmtNodeCostPerGPUHr = 'avg(avg_over_time(node_gpu_hourly_cost{%s}[%s:%s])) by (node, instance_type, provider_id)'

# Determines if nodes are spot instances over a time period.
queryFmtNodeIsSpot = 'avg_over_time(kubecost_node_is_spot{%s}[%s:%s])'

# Retrieves information about PersistentVolumeClaims (PVCs).
queryFmtPVCInfo = 'avg(kube_persistentvolumeclaim_info{volumename != ""}) by (persistentvolumeclaim, storageclass, volumename, namespace)[%s:%s]'

# Calculates the average PersistentVolumeClaim (PVC) allocation to pods over time.
queryFmtPodPVCAllocation = 'avg(avg_over_time(pod_pvc_allocation{%s}[%s:%s])) by (persistentvolume, persistentvolumeclaim, pod, namespace)'

# Calculates the average storage requested by PVCs over time.
queryFmtPVCBytesRequested = 'avg(avg_over_time(kube_persistentvolumeclaim_resource_requests_storage_bytes{%s}[%s:%s])) by (persistentvolumeclaim, namespace)'

# Counts the number of active PersistentVolumes (PVs) within a time range.
queryFmtPVActiveMins = 'count(kube_persistentvolume_capacity_bytes{%s}) by (persistentvolume)[%s:%s]'

# Calculates the average capacity of PersistentVolumes (PVs) over time.
queryFmtPVBytes = 'avg(avg_over_time(kube_persistentvolume_capacity_bytes{%s}[%s:%s])) by (persistentvolume)'

# Calculates the average cost per GiB per hour for PersistentVolumes (PVs).
queryFmtPVCostPerGiBHour = 'avg(avg_over_time(pv_hourly_cost{%s}[%s:%s])) by (volumename)'

# Retrieves metadata information for PersistentVolumes (PVs) over time.
queryFmtPVMeta = 'avg(avg_over_time(kubecost_pv_info{%s}[%s:%s])) by (%s, persistentvolume, provider_id)'

# Calculates the total data transferred between zones within the same region over time.
queryFmtNetZoneGiB = 'sum(increase(kubecost_pod_network_egress_bytes_total{internet="false", same_zone="false", same_region="true"}[%s:%s])) by (pod_name, namespace) / 1024 / 1024 / 1024'

# Calculates the average cost per GiB for network egress between zones within the same region.
queryFmtNetZoneCostPerGiB = 'avg(avg_over_time(kubecost_network_zone_egress_cost{%s}[%s:%s])) by (%s)'

# Calculates the total data transferred between regions over time.
queryFmtNetRegionGiB = 'sum(increase(kubecost_pod_network_egress_bytes_total{internet="false", same_zone="false", same_region="false"}[%s:%s])) by (pod_name, namespace) / 1024 / 1024 / 1024'

# Calculates the average cost per GiB for network egress between regions.
queryFmtNetRegionCostPerGiB = 'avg(avg_over_time(kubecost_network_region_egress_cost{%s}[%s:%s])) by (%s)'

# Calculates the total data transferred to the internet over time.
queryFmtNetInternetGiB = 'sum(increase(kubecost_pod_network_egress_bytes_total{internet="true"}[%s:%s])) by (pod_name, namespace) / 1024 / 1024 / 1024'

# Calculates the average cost per GiB for network egress to the internet.
queryFmtNetInternetCostPerGiB = 'avg(avg_over_time(kubecost_network_internet_egress_cost{%s}[%s:%s])) by (%s)'

# Calculates the total data received by pods over time.
queryFmtNetReceiveBytes = 'sum(increase(container_network_receive_bytes_total{pod!=""}[%s:%s])) by (pod_name, pod, namespace)'

# Calculates the total data transmitted by pods over time.
queryFmtNetTransferBytes = 'sum(increase(container_network_transmit_bytes_total{pod!=""}[%s:%s])) by (pod_name, pod, namespace)'

# Retrieves the labels for nodes over a specified time period.
queryFmtNodeLabels = 'avg_over_time(kube_node_labels{%s}[%s:%s])'

# Retrieves the labels for namespaces over a specified time period.
queryFmtNamespaceLabels = 'avg_over_time(kube_namespace_labels{%s}[%s:%s])'

# Retrieves the annotations for namespaces over a specified time period.
queryFmtNamespaceAnnotations = 'avg_over_time(kube_namespace_annotations{%s}[%s:%s])'

# Retrieves the labels for pods over a specified time period.
queryFmtPodLabels = 'avg_over_time(kube_pod_labels{%s}[%s:%s])'

# Retrieves the annotations for pods over a specified time period.
queryFmtPodAnnotations = 'avg_over_time(kube_pod_annotations{%s}[%s:%s])'

# Retrieves the labels for services over a specified time period.
queryFmtServiceLabels = 'avg_over_time(service_selector_labels{%s}[%s:%s])'

# Retrieves the labels for deployments over a specified time period.
queryFmtDeploymentLabels = 'avg_over_time(deployment_match_labels{%s}[%s:%s])'

# Retrieves the labels for StatefulSets over a specified time period.
queryFmtStatefulSetLabels = 'avg_over_time(statefulSet_match_labels{%s}[%s:%s])'

# Retrieves the number of DaemonSet pods over a specified time period.
queryFmtDaemonSetLabels = 'sum(avg_over_time(kube_pod_owner{owner_kind="DaemonSet"}[%s:%s])) by (pod, owner_name, namespace)'

# Retrieves the number of Job pods over a specified time period.
queryFmtJobLabels = 'sum(avg_over_time(kube_pod_owner{owner_kind="Job"}[%s:%s])) by (pod, owner_name, namespace)'

# Retrieves the number of ReplicaSet pods over a specified time period.
queryFmtPodsWithReplicaSetOwner = 'sum(avg_over_time(kube_pod_owner{owner_kind="ReplicaSet"}[%s:%s])) by (pod, owner_name, namespace)'

# Retrieves the number of ReplicaSets without owners over a specified time period.
queryFmtReplicaSetsWithoutOwners = 'avg(avg_over_time(kube_replicaset_owner{owner_kind="<none>", owner_name="<none>"}[%s:%s])) by (replicaset, namespace)'

# Retrieves the labels for ReplicaSets with Rollout owners over a specified time period.
queryFmtReplicaSetsWithRolloutOwner = 'avg(avg_over_time(kube_replicaset_owner{owner_kind="Rollout"}[%s:%s])) by (replicaset, namespace, owner_kind, owner_name)'

# Calculates the average cost per hour for load balancers.
queryFmtLBCostPerHr = 'avg(avg_over_time(kubecost_load_balancer_cost{%s}[%s:%s])) by (namespace, service_name, ingress_ip)'

# Counts the number of active minutes for load balancers within a time range.
queryFmtLBActiveMins = 'count(kubecost_load_balancer_cost{%s}) by (namespace, service_name)[%s:%s]'

# Retrieves the timestamp of the oldest sample for node CPU costs within a time range.
queryFmtOldestSample = 'min_over_time(timestamp(group(node_cpu_hourly_cost{%s}))[%s:%s])'

# Retrieves the timestamp of the newest sample for node CPU costs within a time range.
queryFmtNewestSample = 'max_over_time(timestamp(group(node_cpu_hourly_cost{%s}))[%s:%s])'
