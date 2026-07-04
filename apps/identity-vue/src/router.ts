import { createRouter, createWebHistory } from 'vue-router'
import Users from './views/Users.vue'
import Groups from './views/Groups.vue'
import AuditLogs from './views/AuditLogs.vue'

const routes = [
  { path: '/', component: Users },
  { path: '/groups', component: Groups },
  { path: '/audit', component: AuditLogs },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
