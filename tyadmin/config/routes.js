[
    {
        name: 'Home',
        path: '/xadmin/index',
        icon: 'dashboard',
        component: './TyAdminBuiltIn/DashBoard'
    },
    {
        path: '/xadmin/',
        redirect: '/xadmin/index',
    },
    {
        name: '认证和授权',
        icon: 'BarsOutlined',
        path: '/xadmin/auth',
        routes:
        [
            {
                name: '权限',
                path: '/xadmin/auth/permission',
                component: './AutoGenPage/PermissionList',
            },
            {
                name: '组',
                path: '/xadmin/auth/group',
                component: './AutoGenPage/GroupList',
            },
            {
                name: '用户',
                path: '/xadmin/auth/user',
                component: './AutoGenPage/UserList',
            }
        ]
    },
    {
        name: 'Captcha',
        icon: 'BarsOutlined',
        path: '/xadmin/captcha',
        routes:
        [
            {
                name: 'captcha store',
                path: '/xadmin/captcha/captcha_store',
                component: './AutoGenPage/CaptchaStoreList',
            }
        ]
    },
    {
        name: 'Tyadmin_Api',
        icon: 'BarsOutlined',
        path: '/xadmin/tyadmin_api',
        routes:
        [
            {
                name: '系统日志',
                path: '/xadmin/tyadmin_api/ty_admin_sys_log',
                component: './AutoGenPage/TyAdminSysLogList',
            },
            {
                name: 'TyAdmin邮箱验证码',
                path: '/xadmin/tyadmin_api/ty_admin_email_verify_record',
                component: './AutoGenPage/TyAdminEmailVerifyRecordList',
            }
        ]
    },
    {
        name: 'News',
        icon: 'BarsOutlined',
        path: '/xadmin/news',
        routes:
        [
            {
                name: 'news',
                path: '/xadmin/news/news',
                component: './AutoGenPage/NewsList',
            }
        ]
    },
    {
        name: '日志管理',
        icon: 'BarsOutlined',
        path: '/xadmin/collectlog',
        routes:
        [
            {
                name: 'log日志',
                path: '/xadmin/collectlog/collect_log',
                component: './AutoGenPage/CollectLogList',
            }
        ]
    },
    {
        name: 'TyadminBuiltin',
        icon: 'VideoCamera',
        path: '/xadmin/sys',
        routes:
        [
            {
                name: 'TyAdminLog',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_sys_log',
                component: './TyAdminBuiltIn/TyAdminSysLogList'
            },
            {
                name: 'TyAdminVerify',
                icon: 'smile',
                path: '/xadmin/sys/ty_admin_email_verify_record',
                component: './TyAdminBuiltIn/TyAdminEmailVerifyRecordList'
            }
        ]
    },
    {
        name: 'passwordModify',
        path: '/xadmin/account/change_password',
        hideInMenu: true,
        icon: 'dashboard',
        component: './TyAdminBuiltIn/ChangePassword',
    },
    {
        component: './404',
    },
]
