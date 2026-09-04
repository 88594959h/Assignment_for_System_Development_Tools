import subprocess
import statistics
import time
import sys

def run_timed(script, runs=2):
    """运行指定脚本多次，返回 (耗时列表, 最后一次输出)"""
    times = []
    output = ""
    for i in range(runs):
        start = time.perf_counter()
        result = subprocess.run(
            [sys.executable, script],
            capture_output=True, text=True
        )
        elapsed = time.perf_counter() - start
        times.append(elapsed)
        output = result.stdout.strip()
        print(f"  {script} 第{i+1}次: {elapsed:.4f}s  |  输出: {output}")
    return times, output

print("=" * 55)
print("       词频程序性能基准测试 (q08)")
print("=" * 55)

print("\n>>> 原始版本 wordfreq.py")
before_times, out1 = run_timed("wordfreq.py", runs=2)
before_median = statistics.median(before_times)

print("\n>>> 优化版本 wordfreq_opt.py")
after_times, out2 = run_timed("wordfreq_opt.py", runs=2)
after_median = statistics.median(after_times)

speedup = before_median / after_median if after_median > 0 else float('inf')

print("\n" + "=" * 55)
print("                 测试结果汇总")
print("=" * 55)
print(f"  原始版本各次耗时:   {[round(t,4) for t in before_times]}")
print(f"  原始版本中位数:     {before_median:.4f} s")
print(f"  优化版本各次耗时:   {[round(t,4) for t in after_times]}")
print(f"  优化版本中位数:     {after_median:.4f} s")
print(f"  加速比:             {speedup:.1f}x")
print(f"  输出一致性检查:     {'PASS ✓' if out1 == out2 else 'FAIL ✗'}")
print(f"    原始输出: {out1}")
print(f"    优化输出: {out2}")
print("=" * 55)
