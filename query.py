


queryFmtRAMBytesAllocated_chart           = """avg_over_time(container_memory_allocation_bytes{container!="", container!="POD", node!=""}[%s])"""
queryFmtRAMRequests_chart                 = """avg_over_time(kube_pod_container_resource_requests{resource="memory", unit="byte", container!="", container!="POD", node!=""}[%s])"""
queryFmtRAMUsageAvg_chart                 = """avg_over_time(container_memory_working_set_bytes{container!="", container_name!="POD", container!="POD"}[%s])"""
queryFmtRAMUsageMax_chart                 = """max(max_over_time(container_memory_working_set_bytes{container!="", container_name!="POD", container!="POD"}[%s])"""
queryFmtCPUCoresAllocated_chart           = """avg_over_time(container_cpu_allocation{container!="", container!="POD", node!=""}[%s])"""
queryFmtCPURequests_chart                 = """avg_over_time(kube_pod_container_resource_requests{resource="cpu", unit="core", container!="", container!="POD", node!=""}[%s])"""
queryFmtCPUUsageAvg_chart                 = """rate(container_cpu_usage_seconds_total{container!="", container_name!="POD", container!="POD"}[%s])"""
queryFmtGPUsRequested_chart               = """avg_over_time(kube_pod_container_resource_requests{resource="nvidia_com_gpu", container!="",container!="POD", node!="")[%s])"""
queryFmtGPUsUsageAvg_chart                = """avg_over_time(DCGM_FI_DEV_GPU_UTIL{container!=""}[%s])"""
queryFmtGPUsAllocated_chart               = """avg_over_time(container_gpu_allocation{container!="", container!="POD", node!=""}[%s])"""