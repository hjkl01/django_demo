import request from 'umi-request';

import { buildFileFormData } from '@/utils/utils'
export async function queryTyAdminEmailVerifyRecord(params) {
  return request('/api/xadmin/v1/ty_admin_email_verify_record', {
    params,
  });
}
export async function removeTyAdminEmailVerifyRecord(params) {
  return request(`/api/xadmin/v1/ty_admin_email_verify_record/${params}`, {
    method: 'DELETE',
  });
}
export async function addTyAdminEmailVerifyRecord(params) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request('/api/xadmin/v1/ty_admin_email_verify_record', {
    method: 'POST',
    data: fileData,
  });
}
export async function updateTyAdminEmailVerifyRecord(params, id) {
  let fileFieldList = []
  let fileData = buildFileFormData(params, fileFieldList);
  return request(`/api/xadmin/v1/ty_admin_email_verify_record/${id}`, {
    method: 'PUT',
    data: fileData,
  });
}
export async function queryTyAdminEmailVerifyRecordVerboseName(params) {
  return request('/api/xadmin/v1/ty_admin_email_verify_record/verbose_name', {
    params,
  });
}
export async function queryTyAdminEmailVerifyRecordListDisplay(params) {
  return request('/api/xadmin/v1/ty_admin_email_verify_record/list_display', {
    params,
  });
}
export async function queryTyAdminEmailVerifyRecordDisplayOrder(params) {
  return request('/api/xadmin/v1/ty_admin_email_verify_record/display_order', {
    params,
  });
}


