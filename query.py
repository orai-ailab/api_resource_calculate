
queryFmtRAMRequests_chart                 = """avg_over_time(kube_pod_container_resource_requests{resource="memory", unit="byte", container!="", container!="POD", node!=""}[%s])"""
queryFmtRAMUsageAvg_chart                 = """avg_over_time(container_memory_working_set_bytes{container!="", container_name!="POD", container!="POD"}[%s])"""

queryFmtCPURequests_chart                 = """avg_over_time(kube_pod_container_resource_requests{resource="cpu", unit="core", container!="", container!="POD", node!=""}[%s])"""
queryFmtCPUUsageAvg_chart                 = """rate(container_cpu_usage_seconds_total{container!="", container_name!="POD", container!="POD"}[%s])"""

queryFmtGPUsRequested_chart               = """avg_over_time(kube_pod_container_resource_requests{resource="nvidia_com_gpu", container!="",container!="POD", node!=""}[%s])"""
queryFmtGPUsUsageAvg_chart                = """avg_over_time(DCGM_FI_PROF_GR_ENGINE_ACTIVE{container!=""}[%s])"""


# queryFmtRAMRequests                 = """avg(avg_over_time(kube_pod_container_resource_requests{resource="memory", unit="byte", container!="", container!="POD", node!=""}[%s])) by (container, pod, namespace, node, %s)"""
# queryFmtRAMUsageAvg                 = """avg(avg_over_time(container_memory_working_set_bytes{container!="", container_name!="POD", container!="POD"}[%s])) by (container_name, container, pod_name, pod, namespace, instance, %s)"""

# queryFmtCPURequests                 = """avg(avg_over_time(kube_pod_container_resource_requests{resource="cpu", unit="core", container!="", container!="POD", node!=""}[%s])) by (container, pod, namespace, node, %s)"""
# queryFmtCPUUsageAvg                 = """avg(rate(container_cpu_usage_seconds_total{container!="", container_name!="POD", container!="POD"}[%s])) by (container_name, container, pod_name, pod, namespace, instance, %s)"""

# queryFmtGPUsRequested               = """avg(avg_over_time(kube_pod_container_resource_requests{resource="nvidia_com_gpu", container!="",container!="POD", node!=""}[%s])) by (container, pod, namespace, node, %s)"""
# queryFmtGPUsUsageAvg                = """avg(avg_over_time(DCGM_FI_PROF_GR_ENGINE_ACTIVE{container!=""}[%s])) by (container, pod, namespace, %s)"""



queryFmtRAMRequests                 = """avg(sum_over_time(kube_pod_container_resource_requests{resource="memory", unit="byte", container!="",container!="POD"}[%s])) by (namespace, container_name, pod_name, %s)"""
queryFmtRAMUsageAvg                 = """avg(sum_over_time(container_memory_working_set_bytes{container!="", container!="POD", instance!=""}[%s])) by (namespace, container_name, pod_name,%s)"""

queryFmtCPURequests                 = """avg(sum_over_time(kube_pod_container_resource_requests{resource="cpu", unit="core", container!="",container!="POD", node!=""}[%s])) by (namespace, container_name, pod_name,%s)"""
queryFmtCPUUsageAvg                 = """avg(rate(container_cpu_usage_seconds_total{container!="", container!="POD", instance!=""}[%s])) by (namespace, container_name, pod_name,%s)"""

queryFmtGPUsRequested               = """avg(sum_over_time(kube_pod_container_resource_requests{resource=~"nvidia_com.+", container!="",container!="POD", node!=""}[%s])) by (namespace, container_name, pod_name,%s)"""
queryFmtGPUsUsageAvg                = """avg(avg_over_time(DCGM_FI_PROF_GR_ENGINE_ACTIVE{container!=""}[%s])) by (container, pod, namespace, %s)"""

