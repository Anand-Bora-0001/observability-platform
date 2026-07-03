import React from 'react';
import { AlertTriangle, Clock, CheckCircle2, ChevronRight } from 'lucide-react';

const mockIncidents = [
  { id: 1042, title: '[CRITICAL] High Memory usage detected', severity: 'critical', status: 'open', time: '10 mins ago', target: 'db-prod-01' },
  { id: 1041, title: '[WARNING] CPU usage is above 85%', severity: 'warning', status: 'investigating', time: '1 hour ago', target: 'web-prod-01' },
  { id: 1040, title: '[CRITICAL] Instance Down', severity: 'critical', status: 'resolved', time: '2 hours ago', target: 'web-prod-02' },
  { id: 1039, title: '[INFO] Scheduled Database Backup', severity: 'info', status: 'closed', time: '1 day ago', target: 'db-prod-01' },
];

const severityColors: Record<string, string> = {
  critical: 'bg-red-500/10 text-red-500 border-red-500/20',
  warning: 'bg-yellow-500/10 text-yellow-500 border-yellow-500/20',
  info: 'bg-blue-500/10 text-blue-500 border-blue-500/20',
};

const statusIcons: Record<string, React.ReactNode> = {
  open: <AlertTriangle size={16} className="text-red-400" />,
  investigating: <Clock size={16} className="text-yellow-400" />,
  resolved: <CheckCircle2 size={16} className="text-green-400" />,
  closed: <CheckCircle2 size={16} className="text-gray-400" />,
};

const Incidents: React.FC = () => {
  return (
    <div className="space-y-6">
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-2xl font-bold text-white">Incidents</h1>
          <p className="text-gray-400">View and manage system alerts and incidents</p>
        </div>
        <button className="px-4 py-2 bg-gray-800 hover:bg-gray-700 text-white font-medium rounded-lg shadow-sm border border-gray-700 transition-colors">
          Create Manual Incident
        </button>
      </div>

      <div className="bg-gray-900 border border-gray-800 rounded-xl overflow-hidden">
        <ul className="divide-y divide-gray-800">
          {mockIncidents.map((incident) => (
            <li key={incident.id} className="hover:bg-gray-800/50 transition-colors">
              <div className="px-6 py-4 flex items-center justify-between">
                <div className="flex items-center space-x-4">
                  <div className="flex-shrink-0 mt-1">
                    {statusIcons[incident.status]}
                  </div>
                  <div>
                    <div className="flex items-center space-x-2">
                      <span className={`px-2 py-0.5 text-xs font-semibold rounded border ${severityColors[incident.severity]}`}>
                        {incident.severity.toUpperCase()}
                      </span>
                      <p className="text-sm font-medium text-white">
                        {incident.title}
                      </p>
                    </div>
                    <div className="mt-1 flex items-center space-x-2 text-xs text-gray-400">
                      <span>#{incident.id}</span>
                      <span>&bull;</span>
                      <span>{incident.target}</span>
                      <span>&bull;</span>
                      <span>{incident.time}</span>
                    </div>
                  </div>
                </div>
                <div>
                  <ChevronRight size={20} className="text-gray-500" />
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default Incidents;
