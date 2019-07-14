// LeanCloudService.cs

using LeanCloud;
using LeanCloud.Realtime;
// 引入 LeanCloud SDK
using UnityEngine;

public class LeanCloudService : MonoBehaviour {
  [SerializeField] private string appId; // LeanCloud AppId, 在控制台中获取
  [SerializeField] private string appKey; // LeanCloud AppKey, 在控制台中获取
  [SerializeField] private string clientId; // Realtime 通讯中一个用户的标识, 一般为用户的 id

  private static LeanCloudService instance;
  private AVRealtime realtime;
  private AVIMClient client;

  public static LeanCloudService Instance => instance;

  void Start() {
    // Singleton
    instance = this;
    DontDestroyOnLoad(this);
    // IMPORTANT: LeanCloud 的存储 SDK 是必须要初始化的
    AVClient.Initialize(appId, appKey);
    // IMPORTANT: 初始化 LeanCloud Realtime
    realtime = new AVRealtime(appId, appKey);
    // OPTIONAL: 开启调试日志
    if (Debug.isDebugBuild) {
      AVClient.HttpLog(Debug.Log);
      AVRealtime.WebSocketLog(Debug.Log);
    }
  }
}