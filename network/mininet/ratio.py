def calculate_bandwidth_delay_ratio(path_A, path_B):
    """
    Calculate the bandwidth-delay product ratio between two paths.
    :param path_A: List containing bandwidth and delay of path A [bandwidth_A, delay_A]
    :param path_B: List containing bandwidth and delay of path B [bandwidth_B, delay_B]
    :return: The ratio of the bandwidth-delay product of path B to path A
    """
    # Extracting bandwidth and delay for path A and B
    bandwidth_A, delay_A = path_A
    bandwidth_B, delay_B = path_B
    
    # Convert delays from ms to seconds for calculation
    delay_A_seconds = 1/(delay_A / 1000.0)
    delay_B_seconds = 1/(delay_B / 1000.0)
    
    # Calculate Bandwidth-Delay Product for both paths
    bdp_A = bandwidth_A * delay_A_seconds
    bdp_B = bandwidth_B * delay_B_seconds
    
    # Calculate the ratio of BDPs
    ratio = bdp_B / bdp_A
    
    return ratio

# # Example usage:
# # Path A [bandwidth in Mbps, delay in ms]
# path_A = [20, 100]  # Direct path r2-r6
# # Path B [bandwidth in Mbps, delay in ms]
# path_B = [50, 40]   # Indirect path r2-r4-r6 through r4

# # Calculate the ratio
# ratio = calculate_bandwidth_delay_ratio(path_A, path_B)
# print("Ratio of BDP (Path B to Path A):", ratio)
