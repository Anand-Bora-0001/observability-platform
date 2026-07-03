import React from 'react';
import { Calendar, Clock, Plus, ShieldAlert } from 'lucide-react';

const Maintenance: React.FC = () => {
  const windows = [
    { id: 1, title: 'Weekly DB Patching', server: 'db-prod-01', start: '2026-07-04 02:00:00', end: '2026-07-04 04:00:00', status: 'upcoming' },
    { id: 2, title: 'Network Switch Upgrade', server: 'All Servers', start: '2026-07-10 01:00:00', end: '2026-07-10 03:00:00', status: 'scheduled' },
  ];

  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-white">Maintenance Windows</h1>
          <p className="text-gray-400">Schedule downtime and suppress alerts</p>
        </div>
        <button className="px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-lg shadow-sm transition-colors flex items-center space-x-2">
          <Plus size={18} />
          <span>Schedule Window</span>
        </button>
      </div>

      <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
        <table className="min-w-full divide-y divide-gray-800">
          <thead className="bg-gray-800/50">
            <tr>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Title</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Target</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Start Time</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">End Time</th>
              <th className="px-6 py-3 text-left text-xs font-medium text-gray-400 uppercase tracking-wider">Status</th>
            </tr>
          </thead>
          <tbody className="bg-gray-900 divide-y divide-gray-800">
            {windows.map((win) => (
              <tr key={win.id} className="hover:bg-gray-800/50 transition-colors">
                <td className="px-6 py-4 whitespace-nowrap text-sm font-medium text-white">
                  <div className="flex items-center space-x-2">
                    <ShieldAlert size={16} className="text-yellow-500" />
                    <span>{win.title}</span>
                  </div>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-300">
                  {win.server}
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-400 flex items-center space-x-2">
                  <Calendar size={14} />
                  <span>{win.start}</span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap text-sm text-gray-400 flex items-center space-x-2">
                  <Clock size={14} />
                  <span>{win.end}</span>
                </td>
                <td className="px-6 py-4 whitespace-nowrap">
                  <span className="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-blue-100 text-blue-800">
                    {win.status.toUpperCase()}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Maintenance;
