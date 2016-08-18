import java.security.MessageDigest;

//获取变量值
String timestamp = vars.get("timestamp");
String uri = vars.get("uri");
String host = vars.get("host");

String appkey = "!W7iwls@B8q2RKz&CJipZNY9n9Me0H@q";
//设置参数
Hashtable hashtable = new Hashtable();
hashtable.put("appId","0");
hashtable.put("deviceType","3");
hashtable.put("appVersion","0.0.1");
hashtable.put("deviceId","0");
hashtable.put("timestamp",timestamp);
hashtable.put("mobile","18825242861");
hashtable.put("verificationCode","999999");

//排序并合并参数数据
static String concatParams(Hashtable hashtable){
	Object[] key = hashtable.keySet().toArray();
	String str = "";
	Arrays.sort(key);
    for (Object newkey : key) {
		String newval = hashtable.get(newkey).toString();
		str += "&" + newkey + "=" + newval;
	}
	return str.replaceFirst("&", "");
}
//二进制转换成16进制
private static String byte2hex( byte[] b ) {
    StringBuffer buf = new StringBuffer();
    int i;
    for( int offset = 0; offset < b.length; offset++ ) {
      i = b[offset];
      if(i < 0) i += 256;
      if(i < 16) buf.append("0");
      buf.append(Integer.toHexString(i));
    }
    return buf.toString();
  }

String params = concatParams(hashtable);
String str = host + uri + "?" + params + "&" + appkey;
MessageDigest md = MessageDigest.getInstance("MD5");
String sign = byte2hex(md.digest(str.getBytes("UTF-8")));

//设置参数sign，给http请求用
vars.put("sign",sign);
