// @ts-nocheck
import { ApplyPluginsType, dynamic } from '/home/jinlong/django_demo/tyadmin/node_modules/@umijs/runtime';
import { plugin } from './plugin';

const routes = [
  {
    "path": "/xadmin/login",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__UserLayout' */'/home/jinlong/django_demo/tyadmin/src/layouts/UserLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "name": "login",
        "path": "/xadmin/login",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__UserLogin' */'/home/jinlong/django_demo/tyadmin/src/pages/TyAdminBuiltIn/UserLogin'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "path": "/xadmin/",
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__SecurityLayout' */'/home/jinlong/django_demo/tyadmin/src/layouts/SecurityLayout'), loading: require('@/components/PageLoading/index').default}),
    "routes": [
      {
        "path": "/xadmin/",
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'layouts__BasicLayout' */'/home/jinlong/django_demo/tyadmin/src/layouts/BasicLayout'), loading: require('@/components/PageLoading/index').default}),
        "authority": [
          "admin",
          "user"
        ],
        "routes": [
          {
            "name": "Home",
            "path": "/xadmin/index",
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__DashBoard' */'/home/jinlong/django_demo/tyadmin/src/pages/TyAdminBuiltIn/DashBoard'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "path": "/xadmin/",
            "redirect": "/xadmin/index",
            "exact": true
          },
          {
            "name": "认证和授权",
            "icon": "BarsOutlined",
            "path": "/xadmin/auth",
            "routes": [
              {
                "name": "权限",
                "path": "/xadmin/auth/permission",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__PermissionList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/PermissionList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "组",
                "path": "/xadmin/auth/group",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__GroupList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/GroupList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "用户",
                "path": "/xadmin/auth/user",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__UserList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/UserList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "Captcha",
            "icon": "BarsOutlined",
            "path": "/xadmin/captcha",
            "routes": [
              {
                "name": "captcha store",
                "path": "/xadmin/captcha/captcha_store",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__CaptchaStoreList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/CaptchaStoreList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "Tyadmin_Api",
            "icon": "BarsOutlined",
            "path": "/xadmin/tyadmin_api",
            "routes": [
              {
                "name": "系统日志",
                "path": "/xadmin/tyadmin_api/ty_admin_sys_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__TyAdminSysLogList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/TyAdminSysLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "TyAdmin邮箱验证码",
                "path": "/xadmin/tyadmin_api/ty_admin_email_verify_record",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__TyAdminEmailVerifyRecordList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/TyAdminEmailVerifyRecordList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "News",
            "icon": "BarsOutlined",
            "path": "/xadmin/news",
            "routes": [
              {
                "name": "news",
                "path": "/xadmin/news/news",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__NewsList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/NewsList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "日志管理",
            "icon": "BarsOutlined",
            "path": "/xadmin/collectlog",
            "routes": [
              {
                "name": "log日志",
                "path": "/xadmin/collectlog/collect_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__AutoGenPage__CollectLogList' */'/home/jinlong/django_demo/tyadmin/src/pages/AutoGenPage/CollectLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "TyadminBuiltin",
            "icon": "VideoCamera",
            "path": "/xadmin/sys",
            "routes": [
              {
                "name": "TyAdminLog",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_sys_log",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminSysLogList' */'/home/jinlong/django_demo/tyadmin/src/pages/TyAdminBuiltIn/TyAdminSysLogList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              },
              {
                "name": "TyAdminVerify",
                "icon": "smile",
                "path": "/xadmin/sys/ty_admin_email_verify_record",
                "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__TyAdminEmailVerifyRecordList' */'/home/jinlong/django_demo/tyadmin/src/pages/TyAdminBuiltIn/TyAdminEmailVerifyRecordList'), loading: require('@/components/PageLoading/index').default}),
                "exact": true
              }
            ]
          },
          {
            "name": "passwordModify",
            "path": "/xadmin/account/change_password",
            "hideInMenu": true,
            "icon": "dashboard",
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__TyAdminBuiltIn__ChangePassword' */'/home/jinlong/django_demo/tyadmin/src/pages/TyAdminBuiltIn/ChangePassword'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          },
          {
            "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/home/jinlong/django_demo/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
            "exact": true
          }
        ]
      },
      {
        "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/home/jinlong/django_demo/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
        "exact": true
      }
    ]
  },
  {
    "component": dynamic({ loader: () => import(/* webpackChunkName: 'p__404' */'/home/jinlong/django_demo/tyadmin/src/pages/404'), loading: require('@/components/PageLoading/index').default}),
    "exact": true
  }
];

// allow user to extend routes
plugin.applyPlugins({
  key: 'patchRoutes',
  type: ApplyPluginsType.event,
  args: { routes },
});

export { routes };
