import React from 'react';
import { Ticket as TicketIcon, User, Clock, CheckCircle } from 'lucide-react';

const mockTickets = [
  { id: 'TKT-1024', title: 'Database connection pooling issue', priority: 'high', status: 'open', assignee: 'Alice Dev', created_at: '2 hours ago' },
  { id: 'TKT-1023', title: 'Update Redis configuration for caching', priority: 'medium', status: 'in_progress', assignee: 'Bob Ops', created_at: '5 hours ago' },
  { id: 'TKT-1022', title: 'False positive alert on Instance Down', priority: 'low', status: 'resolved', assignee: 'Charlie SRE', created_at: '1 day ago' },
  { id: 'TKT-1021', title: 'Add SLA report export feature', priority: 'medium', status: 'closed', assignee: 'Unassigned', created_at: '2 days ago' },
];

const priorityColors: Record<string, string> = {
  critical: 'bg-red-500/10 text-red-500 border-red-500/20',
  high: 'bg-orange-500/10 text-orange-500 border-orange-500/20',
  medium: 'bg-blue-500/10 text-blue-500 border-blue-500/20',
  low: 'bg-gray-500/10 text-gray-400 border-gray-500/20',
};

const statusColors: Record<string, string> = {
  open: 'text-red-400',
  in_progress: 'text-yellow-400',
  resolved: 'text-green-400',
  closed: 'text-gray-500',
};

const Tickets: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-white">Support Tickets</h1>
          <p className="text-gray-400">Manage operations tasks and user reports</p>
        </div>
        <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg shadow-sm transition-colors flex items-center space-x-2">
          <TicketIcon size={18} />
          <span>New Ticket</span>
        </button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-6">
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Open Tickets</p>
          <p className="text-2xl font-bold text-white mt-1">12</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Unassigned</p>
          <p className="text-2xl font-bold text-white mt-1">3</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Avg Resolution Time</p>
          <p className="text-2xl font-bold text-white mt-1">4.2h</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 rounded-lg p-4">
          <p className="text-gray-400 text-sm">Current SLA Uptime</p>
          <p className="text-2xl font-bold text-green-400 mt-1">99.98%</p>
        </div>
      </div>

      <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
        <table className="min-w-full divide-y divide-gray-800">
          <thead className="bg-gray-800/50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Ticket</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Status</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Priority</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Assignee</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Created</th>
            </tr>
          </thead>
          <tbody className="bg-gray-900 divide-y divide-gray-800">
            {mockTickets.map((ticket) => (
              <tr key={ticket.id} className="hover:bg-gray-800/50 transition-colors">
                <td className="px-6 py-4">
                  <div className="flex flex-col">
                    <span className="text-sm font-medium text-white">{ticket.title}</span>
                    <span className="text-xs text-gray-500">{ticket.id}</span>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <div className={`flex items-center space-x-2 text-sm font-medium ${statusColors[ticket.status]}`}>
                    {ticket.status === 'resolved' || ticket.status === 'closed' ? <CheckCircle size={16} /> : <Clock size={16} />}
                    <span>{ticket.status.replace('_', ' ').toUpperCase()}</span>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className={`px-2 py-0.5 text-xs font-semibold rounded border ${priorityColors[ticket.priority]}`}>
                    {ticket.priority.toUpperCase()}
                  </span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300 flex items-center space-x-2">
                  <User size={16} className="text-gray-500"/>
                  <span>{ticket.assignee}</span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-400">
                  {ticket.created_at}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Tickets;
