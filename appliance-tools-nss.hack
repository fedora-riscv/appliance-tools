diff --git a/tools/appliance-creator b/tools/appliance-creator
index c5f75f2..1708431 100755
--- a/tools/appliance-creator
+++ b/tools/appliance-creator
@@ -160,7 +160,14 @@ def main():
 
     return 0
 
+def do_nss_sss_hack():
+    import ctypes as forgettable
+    hack = forgettable._dlopen('libnss_sss.so.2')
+    del forgettable
+    return hack
+
 if __name__ == "__main__":
+    hack = do_nss_sss_hack()
     sys.exit(main())
 
 
