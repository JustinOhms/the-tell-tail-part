def trailing_zeros(n):
    """Count trailing zeros in binary representation."""
    count = 0
    while n % 2 == 0:
        n //= 2
        count += 1
    return count

def apply_collatz_step(n):
    """Apply f(n): (3n + 1) / 2^k where k = trailing zeros."""
    n = 3 * n + 1
    k = trailing_zeros(n)
    n //= (1 << k)
    return n, k

def analyze_k_bit_odd_permutations(k):
    """Analyze odd k-bit numbers for tail collapse dominance."""
    failures = []
    total_numbers = 0
    end = 1 << k  # One past largest k-bit number

    print(f"\nAnalyzing odd numbers 1 to {end-1} (k={k}):\n")
    header1 = f"{'Decimal':<8} {'Binary':<{k+2}} "
    header2 = f"{'Win After':<10} {'Max Bits':<10} "
    header3 = f"{'Head Grow':<10} {'Extra Zeros':<12} "
    header4 = f"{'End Dec':<8} {'End Bin':<{k+2}}"
    print(header1 + header2 + header3 + header4)
    
    sep1 = f"{'-'*8} {'-'*(k+2)} "
    sep2 = f"{'-'*10} {'-'*10} "
    sep3 = f"{'-'*10} {'-'*12} "
    sep4 = f"{'-'*8} {'-'*(k+2)}"
    print(sep1 + sep2 + sep3 + sep4)
    
    def bit_length(n):
        """Return bits needed to represent integer n."""
        return n.bit_length()

    # Start at 3, analyze all odd numbers to 2^k-1
    for n in range(3, end, 2):  
        total_numbers += 1
        orig_n = n
        iterations = 0
        zeros_stripped = 0
        total_tail_bits = 0
        head_growth_count = 0  # Track head growth events
        current = n
        tail_win_iteration = None
        max_bits = bit_length(n)  # Initial bit count
        prev_bits = max_bits  # Track previous bit count
        sequence = [n]  # Track sequence for max bit calc
        
        # Track until we reach 1 or tail collapse wins
        while current != 1:
            current, zeros_this_step = apply_collatz_step(current)
            sequence.append(current)
            zeros_stripped += zeros_this_step
            total_tail_bits += zeros_this_step  
            iterations += 1
            
            # Update max bits if current has more bits
            current_bits = bit_length(current)
            
            # Check if head has grown
            if current_bits > prev_bits:
                head_growth_count += 1
                
            prev_bits = current_bits
            max_bits = max(max_bits, current_bits)

            # Calculate extra zeros beyond the guaranteed minimum
            # Every iteration removes at least 1 zero, so extra_zeros = total - iterations
            extra_zeros = zeros_stripped - iterations
            
            if (extra_zeros > 0 and 
                tail_win_iteration is None):
                # Record when extra tail collapse dominates
                tail_win_iteration = iterations  
                break

        # Get ending number (last in sequence or current)
        if sequence and tail_win_iteration is None:
            ending_number = sequence[-1]
        else:
            ending_number = current
            
        # Pad binary to at least k bits for consistency
        max_bits_for_format = max(k, bit_length(ending_number))
        ending_binary = format(ending_number, 
                              f'0{max_bits_for_format}b')
        
        # If reached 1 without tail collapse winning
        if tail_win_iteration is None:
            failure_data = (orig_n, format(orig_n, f'0{k}b'), 
                           zeros_stripped, iterations, 
                           max_bits, head_growth_count, 
                           total_tail_bits, ending_number, 
                           ending_binary)
            failures.append(failure_data)
            win_after = "Never"
        else:
            win_after = f"{tail_win_iteration}"
        
        # Print details for this number
        # Calculate extra zeros for display
        extra_zeros_display = zeros_stripped - iterations if tail_win_iteration else zeros_stripped - iterations
        
        # Print details for this number
        col1 = f"{orig_n:<8} {format(orig_n, f'0{k}b'):<{k+2}} "
        col2 = f"{win_after:<10} {max_bits:<10} "
        col3 = f"{head_growth_count:<10} {extra_zeros_display:<12} "
        col4 = f"{ending_number:<8} {ending_binary:<{k+2}}"
        print(col1 + col2 + col3 + col4)
        
    # Report summary results
    print("\nSummary:")
    if failures:
        msg1 = f"Found {len(failures)} out of {total_numbers} "
        msg2 = "odd numbers where extra zeros (beyond guaranteed minimum) "
        msg3 = "did not exceed zero:"
        print(msg1 + msg2 + msg3)
        
        for (decimal, bits, zeros, iters, max_bits, 
             head_growth, total_tail, end_dec, end_bin) in failures:
            extra_zeros = zeros - iters
            info1 = f"Decimal: {decimal}, Binary: {bits}, "
            info2 = f"Total Zeros: {zeros}, Iterations: {iters}, "
            info3 = f"Extra Zeros: {extra_zeros}, Max Bits: {max_bits}, "
            info4 = f"Head Growth: {head_growth}"
            print(info1 + info2 + info3 + info4)
    else:
        msg1 = f"All {total_numbers} odd numbers exhibited "
        msg2 = "extra zero dominance (removing more zeros than the guaranteed minimum)!"
        print(msg1 + msg2)

if __name__ == "__main__":
    import argparse
    
    # Set up command-line argument parsing
    desc1 = 'Analyze Collatz tail collapse vs '
    desc2 = 'head growth for odd numbers.'
    parser = argparse.ArgumentParser(description=desc1 + desc2)
    
    help_text = 'Maximum number of bits to analyze (default: 16)'
    parser.add_argument('-k', '--bits', type=int, default=16, 
                        help=help_text)
    
    args = parser.parse_args()
    
    # Run the analysis with the specified k value
    analyze_k_bit_odd_permutations(args.bits)
